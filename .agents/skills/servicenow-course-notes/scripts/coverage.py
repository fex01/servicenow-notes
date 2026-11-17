#!/usr/bin/env python3
"""Create and check a reviewable source-to-notes coverage manifest."""
import argparse
import hashlib
import json
from pathlib import Path
import sys
from markdown_util import anchors

def create(inventory):
    records=[]
    for source in inventory['sources']:
        if 'pages' in source:
            location=source['file'] + ':pdf-review'
            identity=hashlib.sha256(location.encode()).hexdigest()[:16]
            records.append({'id':identity,'source':source['file'],'source_sha256':source['sha256'],'line':None,'title':'PDF source coverage and visual review','status':'unresolved','target_anchor':'','prerequisites':[],'dependency_alternatives':{},'optional':False,'reason':'Inspect PDF pages and add lesson and lab items manually.'})
        for heading in source.get('headings',[]):
            location=f"{source['file']}:{heading['line']}"
            identity=hashlib.sha256((location+'\0'+heading['title']).encode()).hexdigest()[:16]
            records.append({'id':identity,'source':source['file'],'source_sha256':source['sha256'],'line':heading['line'],'title':heading['title'],'status':'candidate','target_anchor':'','prerequisites':[],'dependency_alternatives':{},'optional':False,'reason':''})
    return {'version':1,'items':records,'note':'Candidates are unreviewed; mark irrelevant headings excluded with a reason. PDF pages and visuals require manual review.'}

def check(manifest, notes):
    items=manifest['items']; ids=[x['id'] for x in items]; aset=anchors(notes.read_text(encoding='utf-8')); issues=[]
    if len(set(ids))!=len(ids): issues.append('duplicate item IDs')
    byid={x['id']:x for x in items}
    for x in items:
        label=x['id']+' '+x.get('title','')
        status=x.get('status')
        if status in ('candidate','unresolved'): issues.append(f'{label}: {status}; review required')
        elif status=='mapped':
            if x.get('target_anchor','').lstrip('#') not in aset: issues.append(f'{label}: missing target anchor {x.get("target_anchor","")}')
        elif status=='excluded':
            if not x.get('reason'): issues.append(f'{label}: exclusion requires a reason')
        else: issues.append(f'{label}: invalid status {status}')
        for dep in x.get('prerequisites',[]):
            if dep not in byid: issues.append(f'{label}: missing prerequisite {dep}')
            elif byid[dep].get('optional') and not x.get('optional') and not str(x.get('dependency_alternatives',{}).get(dep,'')).strip(): issues.append(f'{label}: depends on optional prerequisite {dep}; record an alternative or mark optional')
    return issues

def main():
    p=argparse.ArgumentParser(description=__doc__); sub=p.add_subparsers(dest='cmd',required=True)
    init=sub.add_parser('init');init.add_argument('inventory',type=Path);init.add_argument('output',type=Path)
    ck=sub.add_parser('check');ck.add_argument('manifest',type=Path);ck.add_argument('notes',type=Path)
    a=p.parse_args()
    try:
        if a.cmd=='init':
            if a.inventory.resolve()==a.output.resolve(): raise ValueError('Output must not overwrite input.')
            data=create(json.loads(a.inventory.read_text(encoding='utf-8')))
            with a.output.open('x',encoding='utf-8') as f: json.dump(data,f,indent=2,ensure_ascii=False);f.write('\n')
            print(f'Created {len(data["items"])} candidate items; manual review required.');return 0
        issues=check(json.loads(a.manifest.read_text(encoding='utf-8')),a.notes)
        for issue in issues: print('WARN:',issue)
        print(f'{len(issues)} issue(s); mappings do not prove semantic completeness.');return bool(issues)
    except (OSError,ValueError,KeyError,json.JSONDecodeError) as e: print(f'Coverage error: {e}',file=sys.stderr);return 1
if __name__=='__main__':sys.exit(main())
