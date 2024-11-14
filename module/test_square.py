import unittest
import sys

sys.path.append("/Документы/geometric_lib")
from square import area, perimeter


class TestSquareArea(unittest.TestCase):
    def test_addition(self):
        # Arrange
        a = 2
        # Act
        expected_result = a * a
        result = area(a)

        # Assert
        self.assertEqual(result, expected_result)


class TestSquarePerimeter(unittest.TestCase):
    def test_addition(self):
        # Arrange
        a = 2
        # Act
        expected_result = 4 * a
        result = perimeter(a)

        # Assert
        self.assertEqual(result, expected_result)
