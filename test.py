import unittest
from main import main

class TestMainFunction(unittest.TestCase):
  def test_main(self):
    self.assertEqual(main(None), "Hello World!")

if _name_=='_main_':
  unittest.main()
