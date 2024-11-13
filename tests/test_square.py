import unittest
from square import area, perimeter


class TestSquare(unittest.TestCase):

    def test_area_positive_side(self):
        a = 4
        expected_area = a * a
        self.assertEqual(area(a), expected_area)

    def test_area_zero_side(self):
        a = 0
        expected_area = 0
        self.assertEqual(area(a), expected_area)

    def test_area_negative_side(self):
        a = -4
        with self.assertRaises(ValueError):
            area(a)

    def test_perimeter_positive_side(self):
        a = 4
        expected_perimeter = 4 * a
        self.assertEqual(perimeter(a), expected_perimeter)

    def test_perimeter_zero_side(self):
        a = 0
        expected_perimeter = 0
        self.assertEqual(perimeter(a), expected_perimeter)

    def test_perimeter_negative_side(self):
        a = -4
        with self.assertRaises(ValueError):
            perimeter(a)


if __name__ == '__main__':
    unittest.main()
