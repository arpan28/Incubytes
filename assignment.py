import unittest


class StringCalculator:
    def Add(self, numbers: str) -> int:
        if not numbers:
            return 0
        

        nums = list(map(int, numbers))
        return sum(n for n in nums)

class TestStringInput(unittest.TestCase):
    def setUp(self):
        self.calc = StringCalculator()

    def test_empty_string(self):
         self.assertEqual(self.calc.Add(""), 0)
    def test_single_number(self):
        self.assertEqual(self.calc.Add("1"), 1)
    
    

    



    
    

if __name__ == "_main_":
    unittest.main()