import unittest
import numpy as np
from pyCAD.cad_kernel.sketch.geometry2.vector import Vector2D


class TestVector2D(unittest.TestCase):
    def test_init(self):
        vector = Vector2D(1.0, 2.0)
        self.assertEqual(vector.x, 1.0)
        self.assertEqual(vector.y, 2.0)

    def test_str(self):
        vector = Vector2D(1.0, 2.0)
        self.assertEqual(str(vector), "(1.0, 2.0)")

    def test_add(self):
        vector1 = Vector2D(1.0, 2.0)
        vector2 = Vector2D(3.0, 4.0)
        result = vector1 + vector2
        self.assertEqual(result.x, 4.0)
        self.assertEqual(result.y, 6.0)

    def test_sub(self):
        vector1 = Vector2D(5.0, 7.0)
        vector2 = Vector2D(2.0, 3.0)
        result = vector1 - vector2
        self.assertEqual(result.x, 3.0)
        self.assertEqual(result.y, 4.0)

    def test_mul(self):
        vector1 = Vector2D(2.0, 3.0)
        scalar = 4.0
        result = vector1 * scalar
        self.assertEqual(result.x, 8.0)
        self.assertEqual(result.y, 12.0)

    def test_truediv(self):
        vector1 = Vector2D(6.0, 8.0)
        scalar = 2.0
        result = vector1 / scalar
        self.assertEqual(result.x, 3.0)
        self.assertEqual(result.y, 4.0)

    def test_magnitude(self):
        vector1 = Vector2D(3.0, 4.0)
        mag = vector1.magnitude()
        self.assertEqual(mag, 5.0)

    def test_dot_product(self):
        vector1 = Vector2D(1.0, 2.0)
        vector2 = Vector2D(3.0, 4.0)
        dot = vector1.dot_product(vector2)
        self.assertEqual(dot, 11.0)

if __name__ == '__main__':
    unittest.main()