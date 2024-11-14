import unittest
import math
import sys

sys.path.append("/Документы/geometric_lib")
from triangle import area, perimeter


class TestTriangleArea(unittest.TestCase):
    def test_addition(self):
        # Arrange
        a = 11
        b = 25
        c = 30
        # Act
        p = (a + b + c) / 2
        expected_result = math.sqrt(p * (p - a) * (p - b) * (p - c))
        result = area(a, b, c)

        # Assert
        self.assertEqual(result, expected_result)


class TestTrianglePerimeter(unittest.TestCase):
    def test_addition(self):
        # Arrange
        a = 11
        b = 30
        c = 25
        # Act
        expected_result = a + b + c
        result = perimeter(a, b, c)

        # Assert
        self.assertEqual(result, expected_result)
