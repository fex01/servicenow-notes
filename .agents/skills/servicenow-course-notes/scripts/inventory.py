#!/usr/bin/env python3
"""Inventory local sources without storing full body text; headings are candidates."""
import argparse
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
from markdown_util import headings

class HTMLInventory(HTMLParser):
    def __init__(self):
        super().__init__(); self.heading=None; self.parts=[]; self.items=[]; self.images=[]; self.hidden=0
    def handle_starttag(self,tag,attrs):
        attrs=dict(attrs)
        if tag in ('script','style','template'): self.hidden+=1
        if not self.hidden and re.fullmatch(r'h[1-6]',tag): self.heading=(tag,self.getpos()[0]); self.parts=[]
        if not self.hidden and tag=='img': self.images.append({'line':self.getpos()[0], 'has_alt':bool(attrs.get('alt'))})
    def handle_endtag(self,tag):
        if tag in ('script','style','template') and self.hidden: self.hidden-=1
        if self.heading and tag==self.heading[0]:
            self.items.append({'line':self.heading[1], 'title':' '.join(''.join(self.parts).split())}); self.heading=None
    def handle_data(self,data):
        if self.heading and not self.hidden: self.parts.append(data)

def inventory(path):
    data=path.read_bytes(); item={'file':str(path),'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),'status':'candidate'}; ext=path.suffix.lower()
    if ext in ('.html','.htm'):
        parser=HTMLInventory(); parser.feed(data.decode('utf-8',errors='replace'))
        item.update(headings=parser.items,images=parser.images,limitation='Candidates only; CSS-hidden and dynamically loaded content need browser review.')
    elif ext in ('.md','.markdown'):
        item['headings']=[{'line':n,'level':level,'title':h} for n,level,h in headings(data.decode('utf-8',errors='replace'))]
    elif ext=='.pdf':
        try: from pypdf import PdfReader
        except ImportError: raise RuntimeError('PDF inventory needs pypdf; use the bundled runtime when available.')
        reader=PdfReader(str(path)); item['pages']=[]
        for n,page in enumerate(reader.pages,1):
            txt=page.extract_text() or ''
            try: images=len(page.images); error=None
            except Exception as exc: images=None; error=str(exc)
            item['pages'].append({'page':n,'text_characters':len(txt.strip()),'image_count':images,'image_error':error,'visual_review':images is None or images>0 or len(txt.strip())<40})
        item['limitation']='No semantic heading extraction; review visually flagged pages and PDF structure.'
    else: raise ValueError('Supported: .html, .htm, .md, .markdown, .pdf')
    return item

def main():
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument('sources',nargs='+',type=Path);ap.add_argument('-o','--output',type=Path,required=True);ap.add_argument('--force',action='store_true',help='replace an existing output')
    args=ap.parse_args()
    try:
        if args.output.resolve() in {p.resolve() for p in args.sources}: raise ValueError('Output must not overwrite a source.')
        if args.output.exists() and not args.force: raise ValueError('Output exists; choose a new path or pass --force.')
        result={'sources':[inventory(p) for p in args.sources]}
        with args.output.open('w' if args.force else 'x',encoding='utf-8') as f: json.dump(result,f,indent=2,ensure_ascii=False);f.write('\n')
    except (OSError,ValueError,RuntimeError) as e: print(str(e),file=sys.stderr);return 1
    print(f'Inventoried {len(args.sources)} source(s) to {args.output}; headings may contain course material.')
    return 0
if __name__=='__main__': sys.exit(main())
