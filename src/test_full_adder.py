import unittest
from unittest.mock import patch
import full_adder

class TestFullAdder(unittest.TestCase):
    
    def test_adder(self):
        result = full_adder.adder("1010","1010")
        unittest.assertEqual(int(result),10100)

if __name__ == "__main__":
    unittest.main()
