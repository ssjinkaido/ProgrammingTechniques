import unittest
from api import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        i = 8
        result = fibonacci(i)
        self.assertEqual(result, 21)
    
    def test_fibonacci_float(self):
        i = 8.5
        with self.assertRaises(TypeError):
            result = fibonacci(i)
    
    def test_fibonacci_string(self):
        i = "aaa"
        with self.assertRaises(TypeError):
            result = fibonacci(i)
    
    def test_fibonacci_negative(self):
        i = -1
        with self.assertRaises(ValueError):
            result = fibonacci(i)
# do it here for fibonacci
