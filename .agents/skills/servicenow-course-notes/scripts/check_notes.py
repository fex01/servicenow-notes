#!/usr/bin/env python3
"""Check common Markdown note issues; a clean result is not a correctness verdict."""
import argparse
from collections import Counter
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
from markdown_util import anchors, headings, visible_lines

def check(path):
    text=path.read_text(encoding='utf-8'); lines=text.splitlines(); warnings=[]
    hs=list(headings(text)); counts=Counter(h for _,_,h in hs); section=None; labs=0
    for h,n in counts.items():
        if n>1: warnings.append(f'duplicate heading: {h}')
    for n,level,h in hs:
        if level == 2: section=h
        if h.startswith('Lab ') and level == 3:
            labs+=1
            if section != 'Labs': warnings.append(f'{n}: lab outside ## Labs')
            following=next((x for x in lines[n:] if x.strip()),'')
            if not following.startswith('🎯 **Goal**:'): warnings.append(f'{n}: lab has no goal line')
        elif section == 'Labs' and level >= 4:
            warnings.append(f'{n}: subheading inside ## Labs: {h}')
    cache={path.resolve():anchors(text)}
    for n,line in visible_lines(text):
        for target in re.findall(r'!?\[[^]]*\]\(\s*(<[^>]+>|[^\s)]+)(?:\s+[^)]*)?\)',line):
            target=target.strip('<>'); parsed=urlsplit(target)
            if parsed.scheme or parsed.netloc: continue
            rel=unquote(parsed.path); anchor=unquote(parsed.fragment)
            dest=(path.parent / rel).resolve() if rel else path.resolve()
            if not dest.exists(): warnings.append(f'{n}: missing local file {rel}'); continue
            if anchor and dest.suffix.lower() in ('.md','.markdown'):
                if dest not in cache: cache[dest]=anchors(dest.read_text(encoding='utf-8'))
                if anchor not in cache[dest]: warnings.append(f'{n}: missing anchor #{anchor} in {rel or path.name}')
    # Count delimiters separately; fences inside list items may be indented.
    active=None
    for n,line in enumerate(lines,1):
        m=re.match(r'^\s{0,4}(`{3,}|~{3,})(.*)$',line)
        if not m: continue
        marker,rest=m.groups()
        if active is None: active=(marker[0],len(marker),n)
        elif marker[0]==active[0] and len(marker)>=active[1] and not rest.strip(): active=None
    if active: warnings.append(f'{active[2]}: unclosed code fence')
    return warnings, len(hs), labs

def main():
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument('notes',type=Path); a=ap.parse_args()
    warnings, count, labs=check(a.notes)
    for w in warnings: print('WARN:',w)
    print(f'Checked {count} headings and {labs} labs; {len(warnings)} warning(s). Limited scanner: review reference-style links and semantic correctness manually.')
    return bool(warnings)
if __name__=='__main__': sys.exit(main())
