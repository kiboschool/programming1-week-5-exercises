import unittest
from main import *


class Test(unittest.TestCase):
    def test_km_to_miles(self):
        self.assertEqual(km_to_miles(3), round(1.8641130000000001, 2))
        self.assertEqual(km_to_miles(10), round(6.21371, 2))
        self.assertEqual(km_to_miles(143.1), round(88.9181901, 2))

    def test_miles_to_km(self):
        self.assertEqual(miles_to_km(3), round(4.82802, 2))
        self.assertEqual(miles_to_km(14.6), round(23.496364, 2))
        self.assertEqual(miles_to_km(-90.5), round(-145.64527, 2))

    def test_lbs_to_kg(self):
        self.assertEqual(lbs_to_kg(6), round(2.721552, 2))
        self.assertEqual(lbs_to_kg(-9), round(-4.082328, 2))
        self.assertEqual(lbs_to_kg(220.4), round(99.9716768, 2))

    def test_kg_to_lbs(self):
        self.assertEqual(kg_to_lbs(5), round(11.0231, 2))
        self.assertEqual(kg_to_lbs(0.96), round(2.116435199999997, 2))
        self.assertEqual(kg_to_lbs(45.5), round(100.31021, 2))


if __name__ == '__main__':
    unittest.main()
