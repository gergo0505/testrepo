import unittest
from math_operations import add, subtract

class TestIntegrationMathOperations(unittest.TestCase):
    def test_add_and_subtract(self):
        result = subtract(add(5, 5), 3)
        self.assertEqual(result, 7)

if __name__ == '__main__':
    unittest.main(
