import unittest


class StringCalculator:
    def Add(self, numbers: str) -> int:
        if not numbers:
            return 0


class TestStringInput(unittest.TestCase):
    def setUp(self):
        self.calc = StringCalculator()

    def test_empty_string(self):
         self.assertEqual(self.calc.Add(""), 0)
    

if __name__ == "_main_":
    unittest.main()