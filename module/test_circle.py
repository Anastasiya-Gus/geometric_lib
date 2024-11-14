import unittest
import math
import sys

sys.path.append("/Документы/geometric_lib")
from circle import area, perimeter


class TestCircleArea(unittest.TestCase):
    def test_addition(self):
        # Arrange
        r = 2
        # Act
        expected_result = math.pi * r * r
        result = area(r)

        # Assert
        self.assertEqual(result, expected_result)


class TestCirclePerimeter(unittest.TestCase):
    def test_addition(self):
        # Arrange
        r = 2
        # Act
        expected_result = 2 * math.pi * r
        result = perimeter(r)

        # Assert
        self.assertEqual(result, expected_result)
