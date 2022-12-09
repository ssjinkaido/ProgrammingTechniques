import unittest
from api import factorial

class TestFactorial(unittest.TestCase):
    def test_factorial_one(self):
        i = 10
        result = factorial(i)
        self.assertEqual(result, 3628800)

    def test_factorial_two(self):
        i = 1
        result = factorial(i)
        self.assertEqual(result, 1)

    def test_factorial_third(self):
        i = 2
        result = factorial(i)
        self.assertEqual(result, 2)
    
    def test_factorial_float(self):
        i = 8.5
        with self.assertRaises(TypeError):
            result = factorial(i)
    
    def test_factorial_string(self):
        i = "aaa"
        with self.assertRaises(TypeError):
            result = factorial(i)
    
    def test_factorial_negative(self):
        i = -1
        with self.assertRaises(ValueError):
            result = factorial(i)

# do it here for factorial
