import importlib.util
import json
import random
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SKILL=Path(__file__).resolve().parents[1]
SCRIPTS=SKILL/'scripts'
sys.path.insert(0,str(SCRIPTS))
from check_notes import check
from coverage import create, check as check_coverage
from inventory import inventory

def run(script,*args):
    return subprocess.run([sys.executable,str(SCRIPTS/script),*map(str,args)],text=True,capture_output=True)

class NotesTests(unittest.TestCase):
    def setUp(self):self.tmp=tempfile.TemporaryDirectory();self.p=Path(self.tmp.name)
    def tearDown(self):self.tmp.cleanup()
    def test_lab_structure_links_and_images(self):
        (self.p/'other.md').write_text('# Found\n')
        f=self.p/'notes.md';f.write_text('# Notes\n### Lab 1.1 - Early\n🎯 **Goal**: A\n## Labs\n### Lab 1.2 - Test\n🎯 **Goal**: B\n#### Forbidden\n![pic](missing.png)\n[bad](other.md#nope)\n')
        warnings,_,_=check(f);joined='\n'.join(warnings)
        for expected in ('lab outside','subheading inside','missing local file','missing anchor'):self.assertIn(expected,joined)
    def test_fence_lengths_and_inventory(self):
        f=self.p/'notes.md';f.write_text('# Course\n````md\n```\n### Lab 1.1 - Fake\n```\n````\n## Labs\n### Lab 1.2 - Real\n🎯 **Goal**: Test\n')
        warnings,_,labs=check(f);self.assertEqual(warnings,[]);self.assertEqual(labs,1)
        names=[x['title'] for x in inventory(f)['headings']];self.assertNotIn('Lab 1.1 - Fake',names);self.assertIn('Lab 1.2 - Real',names)
    def test_html_ignores_scripts(self):
        f=self.p/'a.html';f.write_text('<h1>Visible</h1><script><h2>Fake</h2></script><p><img src="a"></p>')
        result=inventory(f);self.assertEqual([x['title'] for x in result['headings']],['Visible']);self.assertEqual(len(result['images']),1)
    def test_no_inventory_overwrite(self):
        f=self.p/'a.md';f.write_text('# Hi');out=self.p/'out.json';out.write_text('keep')
        r=run('inventory.py',f,'-o',out);self.assertNotEqual(r.returncode,0);self.assertEqual(out.read_text(),'keep')
    def test_coverage_detects_gaps(self):
        f=self.p/'course.md';f.write_text('# First\n## Second\n');notes=self.p/'notes.md';notes.write_text('# Notes\n## First\n')
        manifest=create({'sources':[inventory(f)]});a,b=manifest['items'];a.update(status='mapped',target_anchor='first',prerequisites=['missing']);b.update(status='mapped',target_anchor='does-not-exist')
        warnings='\n'.join(check_coverage(manifest,notes));self.assertIn('missing prerequisite',warnings);self.assertIn('missing target anchor',warnings)
        b.update(optional=True,target_anchor='first');a['prerequisites']=[b['id']]
        self.assertIn('optional prerequisite','\n'.join(check_coverage(manifest,notes)))
        a['dependency_alternatives']={b['id']:'Create fixture manually'}
        self.assertNotIn('optional prerequisite','\n'.join(check_coverage(manifest,notes)))

@unittest.skipUnless(importlib.util.find_spec('pypdf') and importlib.util.find_spec('PIL') and importlib.util.find_spec('reportlab'),'PDF regression needs pypdf, Pillow and reportlab')
class PDFTests(unittest.TestCase):
    def setUp(self):self.tmp=tempfile.TemporaryDirectory();self.p=Path(self.tmp.name)
    def tearDown(self):self.tmp.cleanup()
    def make_pdf(self,masked=True):
        from PIL import Image
        from reportlab.pdfgen import canvas
        from pypdf import PdfWriter
        from pypdf.generic import DecodedStreamObject, NameObject
        r=random.Random(42);w,h=400,300
        data=bytes(r.randrange(256) for _ in range(w*h*3));im=Image.frombytes('RGB',(w,h),data)
        if masked:
            im=im.convert('RGBA');im.putalpha(Image.frombytes('L',(w,h),bytes((i%w)*255//(w-1) for i in range(w*h))))
        img=self.p/'img.png';im.save(img);original=self.p/'reportlab.pdf'
        c=canvas.Canvas(str(original));c.drawString(30,800,'Readable text');c.drawImage(str(img),30,400,400,300,mask='auto');c.showPage();c.save()
        # Re-encode test image with a single Flate filter to exercise the optimizer.
        writer=PdfWriter(clone_from=str(original));image=writer.pages[0].images[0];ref=image.indirect_reference;obj=ref.get_object();stream=DecodedStreamObject();stream.set_data(obj.get_data())
        for k,v in obj.items():
            if k not in ('/Filter','/Length','/DecodeParms'):stream[NameObject(k)]=v
        writer._objects[ref.idnum-1]=stream.flate_encode()
        src=self.p/'source.pdf';writer.write(str(src));return src
    def test_soft_mask_preserved_and_reduces_size(self):
        from pypdf import PdfReader
        src=self.make_pdf();dst=self.p/'out.pdf';r=run('pdf_optimize.py',src,dst,'--mode','balanced')
        self.assertEqual(r.returncode,0,r.stderr);report=json.loads(r.stdout)
        self.assertEqual(report['masked_images'],1);self.assertTrue(all(report['checks'].values()));self.assertLess(dst.stat().st_size,src.stat().st_size)
        x=PdfReader(str(src)).pages[0].images[0].image;y=PdfReader(str(dst)).pages[0].images[0].image
        self.assertEqual(x.size,y.size);self.assertEqual(x.getchannel('A').tobytes(),y.getchannel('A').tobytes())
    def test_nested_bookmarks_and_link_destinations(self):
        from reportlab.pdfgen import canvas
        src=self.p/'links.pdf';c=canvas.Canvas(str(src))
        c.bookmarkPage('first');c.addOutlineEntry('First','first',level=0);c.drawString(40,750,'First')
        c.linkURL('https://example.org', (40,700,150,720));c.linkRect('', 'second',(40,650,150,680),relative=0);c.showPage()
        c.bookmarkPage('second');c.addOutlineEntry('Second','second',level=1);c.drawString(40,750,'Second');c.save()
        dst=self.p/'out.pdf';r=run('pdf_optimize.py',src,dst,'--mode','lossless')
        self.assertEqual(r.returncode,0,r.stderr+r.stdout);self.assertTrue(json.loads(r.stdout)['checks']['features'])
    def test_pdf_inventory_coverage_cannot_be_empty(self):
        source=self.make_pdf();data=inventory(source);manifest=create({'sources':[data]});notes=self.p/'notes.md';notes.write_text('# Notes\n')
        self.assertGreater(len(manifest['items']),0);self.assertIn('unresolved','\n'.join(check_coverage(manifest,notes)))
    def test_form_refused(self):
        from reportlab.pdfgen import canvas
        src=self.p/'form.pdf';c=canvas.Canvas(str(src));c.acroForm.textfield(name='test',x=20,y=500);c.showPage();c.save()
        dst=self.p/'out.pdf';r=run('pdf_optimize.py',src,dst,'--mode','balanced');self.assertNotEqual(r.returncode,0);self.assertFalse(dst.exists())
    def test_output_no_overwrite(self):
        src=self.make_pdf(False);dst=self.p/'exists.pdf';dst.write_text('keep');r=run('pdf_optimize.py',src,dst);self.assertNotEqual(r.returncode,0);self.assertEqual(dst.read_text(),'keep')
    def test_inventory_pdf_marks_mixed_page(self):
        result=inventory(self.make_pdf());self.assertTrue(result['pages'][0]['visual_review']);self.assertGreater(result['pages'][0]['image_count'],0);self.assertGreater(result['pages'][0]['text_characters'],0)

if __name__=='__main__':unittest.main()
