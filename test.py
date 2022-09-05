import unittest
from main import *

class Test(unittest.TestCase):
    def test_basic_list(self):
        l = [3,2,4,5]
        result = smallest_list_item(l)
        self.assertEqual(result, 2)

    def test_with_floats(self):
        l = [3.0, 2.7, 2.4, 50.0, 4.6, 6.5, 8.5]
        result = smallest_list_item(l)
        self.assertEqual(result, 2.4)

    def test_with_negatives(self):
        l = [3.0, 2.7, -2.4, 50.0, -4.6, -6.5, 8.5]
        result = smallest_list_item(l)
        self.assertEqual(result, -6.5)

if __name__ == '__main__':
    unittest.main()
