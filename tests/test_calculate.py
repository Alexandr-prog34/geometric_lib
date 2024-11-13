import unittest
from unittest.mock import patch
from calculate import calc


class TestCalculate(unittest.TestCase):

    def test_circle_area(self):
        with patch('builtins.print') as mocked_print:
            result = calc('circle', 'area', [5])
            self.assertAlmostEqual(result, 78.53981633974483)
            mocked_print.assert_called_with(
                'Area of circle with size(s) [5] is 78.53981633974483'
            )

    def test_circle_perimeter(self):
        with patch('builtins.print') as mocked_print:
            result = calc('circle', 'perimeter', [5])
            self.assertAlmostEqual(result, 31.41592653589793)
            mocked_print.assert_called_with(
                'Perimeter of circle with size(s) [5] is 31.41592653589793'
            )

    def test_square_area(self):
        with patch('builtins.print') as mocked_print:
            result = calc('square', 'area', [4])
            self.assertEqual(result, 16)
            mocked_print.assert_called_with(
                'Area of square with size(s) [4] is 16'
            )

    def test_square_perimeter(self):
        with patch('builtins.print') as mocked_print:
            result = calc('square', 'perimeter', [4])
            self.assertEqual(result, 16)
            mocked_print.assert_called_with(
                'Perimeter of square with size(s) [4] is 16'
            )

    def test_triangle_area(self):
        with patch('builtins.print') as mocked_print:
            result = calc('triangle', 'area', [3, 4, 5])
            self.assertAlmostEqual(result, 6.0)
            mocked_print.assert_called_with(
                'Area of triangle with size(s) [3, 4, 5] is 6.0'
            )

    def test_triangle_perimeter(self):
        with patch('builtins.print') as mocked_print:
            result = calc('triangle', 'perimeter', [3, 4, 5])
            self.assertEqual(result, 12)
            mocked_print.assert_called_with(
                'Perimeter of triangle with size(s) [3, 4, 5] is 12'
            )

    # Error handling tests

    def test_invalid_figure(self):
        with self.assertRaises(ValueError) as context:
            calc('hexagon', 'area', [5])
        self.assertIn(
            "Фигура 'hexagon' недоступна", str(context.exception)
        )

    def test_invalid_function(self):
        with self.assertRaises(ValueError) as context:
            calc('circle', 'volume', [5])
        self.assertIn(
            "Функция 'volume' недоступна", str(context.exception)
        )

    def test_negative_size_circle(self):
        with self.assertRaises(ValueError) as context:
            calc('circle', 'area', [-5])
        self.assertIn(
            "Радиус не может быть отрицательным", str(context.exception)
        )

    def test_negative_size_square(self):
        with self.assertRaises(ValueError) as context:
            calc('square', 'area', [-4])
        self.assertIn(
            "Сторона квадрата не может быть отрицательной", str(context.exception)
        )

    def test_negative_size_triangle(self):
        with self.assertRaises(ValueError) as context:
            calc('triangle', 'area', [3, -4, 5])
        self.assertIn(
            "Стороны треугольника не могут быть отрицательными", str(context.exception)
        )

    def test_triangle_inequality(self):
        with self.assertRaises(ValueError) as context:
            calc('triangle', 'area', [1, 2, 10])
        self.assertIn(
            "Стороны не образуют треугольник", str(context.exception)
        )

    def test_incorrect_parameter_count_circle(self):
        with self.assertRaises(ValueError) as context:
            calc('circle', 'area', [3, 4])
        self.assertIn(
            "Для фигуры 'circle' требуется 1 параметр", str(context.exception)
        )

    def test_incorrect_parameter_count_triangle(self):
        with self.assertRaises(ValueError) as context:
            calc('triangle', 'area', [3, 4])
        self.assertIn(
            "Для фигуры 'triangle' требуется 3 параметр", str(context.exception)
        )


if __name__ == "__main__":
    unittest.main()
