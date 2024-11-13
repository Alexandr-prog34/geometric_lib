import unittest
from triangle import area, perimeter
import math

class TestTriangle(unittest.TestCase):
    def test_area_valid_triangle(self):
        a, b, c = 3, 4, 5
        s = (a + b + c) / 2
        expected_area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        self.assertAlmostEqual(area(a, b, c), expected_area)

    def test_area_zero_side(self):
        a, b, c = 0, 4, 5
        with self.assertRaises(ValueError):
            area(a, b, c)

    def test_area_invalid_triangle(self):
        a, b, c = 1, 2, 3
        with self.assertRaises(ValueError):
            area(a, b, c)

    def test_area_negative_side(self):
        a, b, c = -3, 4, 5
        with self.assertRaises(ValueError):
            area(a, b, c)

    def test_perimeter_valid_triangle(self):
        a, b, c = 3, 4, 5
        expected_perimeter = a + b + c
        self.assertEqual(perimeter(a, b, c), expected_perimeter)

    def test_perimeter_zero_side(self):
        a, b, c = 0, 4, 5
        with self.assertRaises(ValueError):
            perimeter(a, b, c)

    def test_perimeter_invalid_triangle(self):
        a, b, c = 1, 2, 3
        with self.assertRaises(ValueError):
            perimeter(a, b, c)

    def test_perimeter_negative_side(self):
        a, b, c = -3, 4, 5
        with self.assertRaises(ValueError):
            perimeter(a, b, c)

if __name__ == '__main__':
    unittest.main()
