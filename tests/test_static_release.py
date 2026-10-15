"""No external network, no secrets, no audio content. Audit only the public release artifact."""
from pathlib import Path
import hashlib, re, unittest

ROOT=Path(__file__).resolve().parents[1]
class ReleaseAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.page=(ROOT/'index.html').read_text()
        cls.sql=(ROOT/'db/001_nova_cloud.sql').read_text()
    def test_page(self):
        self.assertTrue(self.page.lstrip().lower().startswith('<!doctype html>'))
        self.assertIn('<html', self.page)
        self.assertIn('</html>', self.page)
    def test_cloud_disabled(self):
        self.assertRegex(self.page, r'window\.NOVA_CLOUD_CONFIG\s*=\s*Object\.freeze')
    def test_no_secrets(self):
        self.assertNotIn('service_role',self.page.lower())
        self.assertNotIn('sk_live_',self.page.lower())
        self.assertNotIn('eyJhbGciOiJIUzI1NiIs',self.page)
        self.assertNotIn('sb_secret_',self.page)
    def test_private_db(self):
        self.assertIn('enable row level security',self.sql)
        self.assertIn("'nova-audio','nova-audio',false",self.sql)
        self.assertIn('nova_select_own',self.sql)
        self.assertIn('nova_insert_own',self.sql)
        self.assertIn('nova_audio_read_own',self.sql)
        self.assertIn('nova_audio_insert_own',self.sql)
    def test_root_entry(self):
        self.assertTrue((ROOT/'.nojekyll').exists())
    def test_no_sensitive_payload(self):
        all_paths=list(ROOT.rglob('*'))
        self.assertFalse(any(p.is_file() and p.suffix.lower() in ('.wav','.mp3','.m4a','.mp4','.aac','.env','.pem','.key') for p in all_paths))
if __name__=='__main__':unittest.main()
