import unittest
import re

class StringCalculator:
    def Add(self, numbers: str) -> int:
        if not numbers:
            return 0
        
        delimiter = r"[,\n]"
        numbers = re.split(delimiter, numbers)
        nums = list(map(int, numbers))
        return sum(n for n in nums)

class TestStringInput(unittest.TestCase):
    def setUp(self):
        self.calc = StringCalculator()

    def test_empty_string(self):
         self.assertEqual(self.calc.Add(""), 0)
    def test_single_number(self):
        self.assertEqual(self.calc.Add("1"), 1)
    
    def test_two_numbers(self):
        self.assertEqual(self.calc.Add("1,2"), 3)

    def test_multiple_numbers(self):
        self.assertEqual(self.calc.Add("1,2,3,4"), 10)
    
    def test_newline_as_delimiter(self):
        self.assertEqual(self.calc.Add("1\n2,3"), 6)



    
    

if __name__ == "_main_":
    unittest.main()