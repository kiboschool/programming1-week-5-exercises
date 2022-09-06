import unittest
from main import *

class Test(unittest.TestCase):
    def test_km_to_miles(self):
        self.assertEqual(km_to_miles(3), 1.8641130000000001)
        self.assertEqual(km_to_miles(10), 6.21371)
        self.assertEqual(km_to_miles(143.1), 88.9181901)

    def test_miles_to_km(self):
        self.assertEqual(miles_to_km(3), 4.82802)
        self.assertEqual(miles_to_km(14.6), 23.496364)
        self.assertEqual(miles_to_km(-90.5), -145.64527)

    def test_lbs_to_kg(self):
        self.assertEqual(lbs_to_kg(6), 2.721552)
        self.assertEqual(lbs_to_kg(-9), -4.082328)
        self.assertEqual(lbs_to_kg(220.4), 99.9716768)

    def test_kg_to_lbs(self):
        self.assertEqual(kg_to_lbs(5), 11.0231)
        self.assertEqual(kg_to_lbs(0.96), 2.1164351999999997)
        self.assertEqual(kg_to_lbs(45.5), 100.31021)

if __name__ == '__main__':
    unittest.main()
