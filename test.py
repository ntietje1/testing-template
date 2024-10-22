# test_simple_methods.py

import unittest
from simple_methods import add, subtract, multiply, divide, square

class TestSimpleMethods(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3, 4), 7)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_square(self):
        # This test will fail deliberately (expected result is wrong)
        self.assertEqual(square(5), 20)  # Should be 25, not 20

if __name__ == '__main__':
    unittest.main()

