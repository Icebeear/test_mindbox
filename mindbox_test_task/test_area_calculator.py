import unittest
from shape_area_calculator import area_calculator

class TestShapes(unittest.TestCase):
    def test_area_calculations(self):
        test_data = {
            (3, ): 28.274333882308138,
            (3, 2, 4, ): 2.9047375096555625,
            (4, 8, ): 32,
        }

        for nums, res in test_data.items():
            self.assertEqual(area_calculator.calculate_area(*nums), res)

    def test_is_triangle(self):
        with self.assertRaises(ValueError):
            area_calculator.calculate_area(1, 2, 3, )

    def test_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            area_calculator.calculate_area(1, 2, 3, 4, )

    def test_is_right_triangle(self):
        test_data = {
            (3, 4, 5, ): True,
            (2, 2, 3, ): False,
        }

        for nums, res in test_data.items():
            self.assertEqual(area_calculator.Triangle(*nums).is_right_triangle(), res)



if __name__ == '__main__':
    unittest.main()