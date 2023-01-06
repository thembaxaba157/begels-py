import unittest
import begels
from io import StringIO
from unittest.mock import patch


class FunctionTests(unittest.TestCase):

    @patch("sys.stdin", StringIO("123\n"))
    def test_get_guess(self):
        returned = begels.get_guess(4)
        self.assertEqual(returned,'123')
    
    
    @patch("sys.stdin",StringIO("222\n123"))
    def test_invalid_get_guess(self):
        returned = begels.get_guess(5)
        self.assertEqual(returned,'123')
    

if __name__ == "__main__":
    unittest.main()
