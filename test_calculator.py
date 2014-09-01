import unittest
from unittest import TestCase
import Calculator
from Calculator import Calculator

class TestCalculator(TestCase):

    def test_returns_string(self):
        self.Calculator = Calculator()
        self.assertIsInstance(self.Calculator.Add(),str)

    def test_empty_string_begets_zero(self):
        self.Calculator = Calculator()
        self.assertEqual("0",self.Calculator.Add(""))

    def test_single_number_returned_back_again(self):
        self.Calculator = Calculator()
        self.assertEqual("2",self.Calculator.Add("2"))

    def test_sum_of_two_numbers_returned(self):
        self.Calculator = Calculator()
        self.assertEqual("3",self.Calculator.Add("1,2"))

    def test_handles_new_line_delimiter(self):
        self.Calculator = Calculator()
        self.assertEqual("3",self.Calculator.Add("1\n2"))
        self.assertEqual("6",self.Calculator.Add("1,2\n3"))

    def test_sequential_delimiters_throws_exception(self):
        self.Calculator = Calculator()
        self.assertRaises(Calculator.InvalidInputException, self.Calculator.Add, "1,\n2")

    def test_custom_delimiters_are_accepted(self):
        self.Calculator = Calculator()
        self.assertEqual("3",self.Calculator.Add("//;\n1;2"))

    def test_custom_and_normal_delimiters(self):
        self.Calculator = Calculator()
        self.assertEqual("15",self.Calculator.Add("//;.\n1\n2;3.4,5"))

    def test_negatives_not_allowed(self):
        self.Calculator = Calculator()
        self.assertRaises(Calculator.NegativesNotAllowedException, self.Calculator.Add, "1,-2")

if __name__ == '__main__':
    unittest.main()