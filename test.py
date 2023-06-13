import unittest
from main import double_elements

from gradescope_utils.autograder_utils.decorators import weight

class Test(unittest.TestCase):
    @weight(0.5)
    def test_double_numeric_elements(self):
        self.assertEqual([], double_elements([]))
        self.assertEqual([2,4,6], double_elements([1,2,3]))
        self.assertEqual([16,1.4,60], double_elements([8,0.7,30]))
        self.assertEqual(list(range(2,100,2)),
                double_elements(list(range(1,50))))
        self.assertEqual(["aa"], double_elements(["a"]))

    @weight(0.5)
    def test_double_alphabetic_elements(self):
        self.assertEqual(["aa"], double_elements(["a"]))
        self.assertEqual(["aa", "bb", "cc"], double_elements(["a", "b", "c"]))

if __name__ == "__main__":
    unittest.main()
