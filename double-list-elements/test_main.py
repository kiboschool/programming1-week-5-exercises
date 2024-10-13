import unittest
from main import double_elements

class Test(unittest.TestCase):
    def test_double_elements(self):
        self.assertEqual([], double_elements([]))
        self.assertEqual([2,4,6], double_elements([1,2,3]))
        self.assertEqual([16,1.4,60], double_elements([8,0.7,30]))
        self.assertEqual(list(range(2,100,2)),
                double_elements(list(range(1,50))))
        self.assertEqual(["aa"], double_elements(["a"]))

if __name__ == "__main__":
    unittest.main()
