import unittest
from calculator import multiply

class TestCalculator(unittest.TestCase):

    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply(-1, -1), 1)

    def test_multiply_positive_and_negative(self):
        self.assertEqual(multiply(5, -2), -10)

    def test_multiply_with_zero(self):
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(5, 0), 0)

if __name__ == '__main__':
    unittest.main()

