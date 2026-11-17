#!/usr/bin/env python3
"""Write a separate PDF candidate. Visual and feature review remain mandatory."""
import argparse
from io import BytesIO
import json
from pathlib import Path
import sys

def document_features(reader):
    from pypdf.generic import ArrayObject, IndirectObject
    page_refs={}
    for index,page in enumerate(reader.pages):
        ref=page.indirect_reference
        if ref is not None: page_refs[(ref.idnum,ref.generation)]=index
    def destination(value):
        if value is None:return None
        if isinstance(value,IndirectObject):
            key=(value.idnum,value.generation)
            if key in page_refs:return {'page':page_refs[key]}
            value=value.get_object()
        if isinstance(value,ArrayObject) or isinstance(value,list):
            return [destination(v) for v in value]
        return str(value)
    def action(annot):
        a=annot.get('/A')
        if not a: return None
        a=a.get_object()
        return {'type':str(a.get('/S','')),'uri':str(a.get('/URI','')),'destination':destination(a.get('/D'))}
    def annotations(page):
        out=[]
        for ref in page.get('/Annots',[]):
            obj=ref.get_object()
            out.append({'subtype':str(obj.get('/Subtype','')),'rect':str(obj.get('/Rect','')),'contents':str(obj.get('/Contents','')),'action':action(obj),'destination':destination(obj.get('/Dest'))})
        return out
    def outline(items):
        result=[]
        for item in items:
            if isinstance(item,list): result.append(outline(item)); continue
            try: page=reader.get_destination_page_number(item)
            except Exception: page=None
            result.append({'title':str(item.get('/Title','')),'page':page,'type':str(item.get('/Type',''))})
        return result
    return {'annotations':[annotations(page) for page in reader.pages],'outline':outline(reader.outline)}

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('source',type=Path);ap.add_argument('output',type=Path);ap.add_argument('--mode',choices=['lossless','balanced'],default='balanced');a=ap.parse_args()
    if a.source.resolve()==a.output.resolve() or a.output.exists():ap.error('Output must be a new file and must not overwrite the source.')
    try:
        import pypdf
        from pypdf import PdfReader,PdfWriter
        from pypdf.generic import NameObject
        if a.mode=='balanced': from PIL import Image
    except ImportError as e: print(f'Missing dependency: {e}; use bundled pypdf and Pillow.',file=sys.stderr);return 2
    try:
        version=tuple(int(x) for x in pypdf.__version__.split('.')[:2])
        if not ((6,0)<=version<(7,0)): raise ValueError(f'pypdf {pypdf.__version__} unsupported; use pypdf >=6,<7.')
        before=PdfReader(str(a.source));root=before.trailer['/Root']
        if before.is_encrypted or any(k in root for k in ('/AcroForm','/Perms','/StructTreeRoot')):raise ValueError('Encrypted PDF, form, signature permissions, or tagged structure detected; use specialized workflow.')
        writer=PdfWriter(clone_from=str(a.source));changed=0;masked=0;skipped=0;seen=set()
        if a.mode=='balanced':
            for page in writer.pages:
                for image in list(page.images):
                    ref=image.indirect_reference
                    if ref is None:skipped+=1;continue
                    key=(ref.idnum,ref.generation)
                    if key in seen:continue
                    seen.add(key);obj=ref.get_object()
                    if any(k in obj for k in ('/Mask','/Decode','/SMaskInData','/ImageMask')) or str(obj.get('/Filter'))!='/FlateDecode':skipped+=1;continue
                    im=image.image
                    if im.mode not in ('RGB','RGBA'):skipped+=1;continue
                    mask=obj.get('/SMask')
                    if im.mode=='RGBA' and mask is None:skipped+=1;continue
                    rgb=im.convert('RGB');buf=BytesIO();rgb.save(buf,format='JPEG',quality=90,subsampling=0,optimize=False)
                    # image.data is a public image-file byte representation, not exact PDF stream size.
                    if len(buf.getvalue())>=len(image.data)*0.8:skipped+=1;continue
                    image.replace(rgb,quality=90,subsampling=0,optimize=False)
                    if mask is not None:ref.get_object()[NameObject('/SMask')]=mask;masked+=1
                    changed+=1
        for page in writer.pages:page.compress_content_streams()
        writer.compress_identical_objects(remove_duplicates=True,remove_unreferenced=True)
        with a.output.open('xb') as f:writer.write(f)
        after=PdfReader(str(a.output))
        checks={'page_count':len(before.pages)==len(after.pages),'text_by_page':len(before.pages)==len(after.pages) and all((x.extract_text() or '')==(y.extract_text() or '') for x,y in zip(before.pages,after.pages)), 'page_boxes':len(before.pages)==len(after.pages) and all((x.mediabox,x.cropbox)==(y.mediabox,y.cropbox) for x,y in zip(before.pages,after.pages)), 'metadata':before.metadata==after.metadata,'features':document_features(before)==document_features(after)}
        print(json.dumps({'input_bytes':a.source.stat().st_size,'output_bytes':a.output.stat().st_size,'mode':a.mode,'lossy_images':changed,'masked_images':masked,'skipped_images':skipped,'checks':checks,'warning':'Visual review and validation of unsupported PDF features remain mandatory.'},indent=2))
        return 0 if all(checks.values()) else 1
    except Exception as e:print(f'Optimization failed: {e}',file=sys.stderr);return 1
if __name__=='__main__':sys.exit(main())
