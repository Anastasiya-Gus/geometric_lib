import unittest
import math
import sys

sys.path.append("/Документы/geometric_lib")
from calculate import calc


class TestCalculate_CircleArea(unittest.TestCase):
    def test_valid_values(self):
        # Arrange
        fig = "circle"
        func = "area"
        size = [5]
        # Act
        expected_result = math.pi * size[0] * size[0]
        result = calc(fig, func, size)
        # Assert
        self.assertAlmostEqual(result, expected_result)

    def test_invalid_values(self):
        # Arrange
        fig = "circle"
        func = "area"
        size = [-5]
        # Act
        expected_result = "The dimensions of the figure must be greater than zero"
        # Assert
        with self.assertRaisesRegex(ValueError, expected_result):
            calc(fig, func, size)

    def test_not_enough_values(self):
        # Arrange
        fig = "circle"
        func = "area"
        size = []
        # Act
        expected_result = "1 parameters are expected for circle and the function area"
        # Assert
        with self.assertRaisesRegex(ValueError, expected_result):
            calc(fig, func, size)


class TestCalculate_CirclePerimeter(unittest.TestCase):
    def test_valid_values(self):
        # Arrange
        fig = "circle"
        func = "perimeter"
        size = [5]
        # Act
        expected_result = 2 * math.pi * size[0]
        result = calc(fig, func, size)
        # Assert
        self.assertAlmostEqual(result, expected_result)

    def test_invalid_values(self):
        # Arrange
        fig = "circle"
        func = "perimeter"
        size = [-5]
        # Act
        expected_result = "The dimensions of the figure must be greater than zero"
        # Assert
        with self.assertRaisesRegex(ValueError, expected_result):
            calc(fig, func, size)

    def test_not_enough_values(self):
        # Arrange
        fig = "circle"
        func = "perimeter"
        size = []
        # Act
        expected_result = (
            "1 parameters are expected for circle and the function perimeter"
        )
        # Assert
        with self.assertRaisesRegex(ValueError, expected_result):
            calc(fig, func, size)


class TestCalculate_SquareArea(unittest.TestCase):
    def test_valid_values(self):
        # Arrange
        fig = "square"
        func = "area"
        size = [25]
        # Act
        expected_result = size[0] * size[0]
        result = calc(fig, func, size)
        # Assert
        self.assertAlmostEqual(result, expected_result)

    def test_invalid_values(self):
        # Arrange
        fig = "square"
        func = "area"
        size = [-25]
        # Act
        expected_result = "The dimensions of the figure must be greater than zero"
        # Assert
        with self.assertRaisesRegex(ValueError, expected_result):
            calc(fig, func, size)

    def test_not_enough_values(self):
        # Arrange
        fig = "square"
        func = "area"
        size = []
        # Act
        expected_result = "1 parameters are expected for square and the function area"
        # Assert
        with self.assertRaisesRegex(ValueError, expected_result):
            calc(fig, func, size)


class TestCalculate_SquarePerimeter(unittest.TestCase):
    def test_valid_values(self):
        # Arrange
        fig = "square"
        func = "perimeter"
        size = [25]
        # Act
        expected_result = 4 * size[0]
        result = calc(fig, func, size)
        # Assert
        self.assertAlmostEqual(result, expected_result)

    def test_invalid_values(self):
        # Arrange
        fig = "square"
        func = "perimeter"
        size = [-25]
        # Act
        expected_result = "The dimensions of the figure must be greater than zero"
        # Assert
        with self.assertRaisesRegex(ValueError, expected_result):
            calc(fig, func, size)

    def test_not_enough_values(self):
        # Arrange
        fig = "square"
        func = "area"
        size = []
        # Act
        expected_result = "1 parameters are expected for square and the function area"
        # Assert
        with self.assertRaisesRegex(ValueError, expected_result):
            calc(fig, func, size)


class TestCalculate_TriangleArea(unittest.TestCase):
    def test_valid_values(self):
        # Arrange
        fig = "triangle"
        func = "area"
        size = [3, 4, 5]
        # Act
        p = (size[0] + size[1] + size[2]) / 2
        expected_result = math.sqrt(p * (p - size[0]) * (p - size[1]) * (p - size[2]))
        result = calc(fig, func, size)
        # Assert
        self.assertAlmostEqual(result, expected_result)

    def test_invalid_values(self):
        # Arrange
        fig = "triangle"
        func = "area"
        size = [3, 4, -5]
        # Act
        expected_result = "The dimensions of the figure must be greater than zero"
        # Assert
        with self.assertRaisesRegex(ValueError, expected_result):
            calc(fig, func, size)

    def test_not_enough_values(self):
        # Arrange
        fig = "triangle"
        func = "area"
        size = [3, 4]
        # Act
        expected_result = "3 parameters are expected for triangle and the function area"
        # Assert
        with self.assertRaisesRegex(ValueError, expected_result):
            calc(fig, func, size)


class TestCalculate_TrianglePerimeter(unittest.TestCase):
    def test_valid_values(self):
        # Arrange
        fig = "triangle"
        func = "perimeter"
        size = [3, 4, 5]
        # Act
        expected_result = size[0] + size[1] + size[2]
        result = calc(fig, func, size)
        # Assert
        self.assertAlmostEqual(result, expected_result)

    def test_invalid_values(self):
        # Arrange
        fig = "triangle"
        func = "perimeter"
        size = [3, 4, -5]
        # Act
        expected_result = "The dimensions of the figure must be greater than zero"
        # Assert
        with self.assertRaisesRegex(ValueError, expected_result):
            calc(fig, func, size)

    def test_not_enough_values(self):
        # Arrange
        fig = "triangle"
        func = "perimeter"
        size = [3, 4]
        # Act
        expected_result = (
            "3 parameters are expected for triangle and the function perimeter"
        )
        # Assert
        with self.assertRaisesRegex(ValueError, expected_result):
            calc(fig, func, size)
