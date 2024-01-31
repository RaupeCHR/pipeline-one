import unittest
from main import main

class TestMainFunction(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main(None), "Hello World!")

if __name__ == '__main__':
    unittest.main()