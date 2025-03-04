import unittest
import re

class StringCalculator:
    def Add(self, numbers: str) -> int:
        if not numbers:
            return 0
        
        delimiter = ','
        if numbers.startswith('//'):
            match = re.match(r'//(\[.*?\]|.)\n(.*)', numbers, re.DOTALL)
            if match:
                delimiters, numbers = match.groups()
                delimiters = re.findall(r'\[(.*?)\]', delimiters) or [delimiters]
                delimiter = '|'.join(map(re.escape, delimiters))
        numbers = re.split(delimiter + '|\n', numbers)
        nums = list(map(int, numbers))
        negatives = [n for n in nums if n < 0]
        if negatives:
            raise ValueError(f"negatives not allowed {negatives}")
        return sum(n for n in nums if n <= 1000)

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

    def test_ignore_numbers_greater_than_1000(self):
        self.assertEqual(self.calc.Add("2,1001"), 2)

    def test_negative_numbers(self):
        with self.assertRaises(ValueError) as context:
            self.calc.Add("1,-2,3,-4")
        self.assertEqual(str(context.exception), "negatives not allowed [-2, -4]")
    
    def test_custom_delimiter(self):
        self.assertEqual(self.calc.Add("//;\n1;2"), 3)

   
if __name__ == "_main_":
    unittest.main()
