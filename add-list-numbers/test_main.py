import unittest
from main import *

class Test(unittest.TestCase):
    def test_numbers_sum_basic(self):
        l = [1,2,3,4,5]
        result = numbers_sum(l)
        self.assertEqual(result, 15)

    def test_floats(self):
        l = [4.1,6.2,9.3,15.4,55.9]
        result = numbers_sum(l)
        self.assertEqual(result, 90.9)

    def test_negatives(self):
        l = [-8.1,1.2,-19.3,5.4,-500.9]
        result = numbers_sum(l)
        self.assertAlmostEqual(result, -521.7)

if __name__ == '__main__':
    unittest.main()
