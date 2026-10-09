import unittest
from app import HUNTS,run_hunt
class HuntTests(unittest.TestCase):
 def test_finds_auth_failure(self): self.assertEqual(run_hunt([{"event_type":"auth_failure"}],HUNTS[0])["match_count"],1)
 def test_case_insensitive(self): self.assertEqual(run_hunt([{"process_name":"PowerShell.exe"}],HUNTS[1])["match_count"],1)
 def test_empty_no_match(self): self.assertEqual(run_hunt([],HUNTS[0])["matches"],[])
 def test_invalid_input(self):
  with self.assertRaises(ValueError): run_hunt({},HUNTS[0])
if __name__=="__main__": unittest.main()
