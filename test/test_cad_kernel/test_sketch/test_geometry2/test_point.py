import unittest
import numpy as np
from src.cad_kernel.sketch.geometry2.point import Point2D
from src.cad_kernel.sketch.geometry2.vector import Vector2D


class TestPoint2D(unittest.TestCase):

    def test_init(self):
        # Create a Point2D
        point = Point2D(1.0, 2.0)

        # Check if the point's position has been set correctly
        self.assertEqual(point.x, 1.0)
        self.assertEqual(point.y, 2.0)

    def test_add_vector(self):
        # Create a Point2D
        point = Point2D(1.0, 2.0)
        
        # Create a Vector2D to add
        vector = Vector2D(3.0, 4.0)

        # Add the vector to the point
        point += vector

        # Check if the point's position has been updated correctly
        self.assertEqual(point.x, 4.0)
        self.assertEqual(point.y, 6.0)

    def test_add_invalid_type(self):
        # Create a Point2D
        point = Point2D(1.0, 2.0)

        # Try to add a Point2D
        with self.assertRaises(TypeError):
            point += Point2D(3.0, 4.0)

if __name__ == '__main__':
    unittest.main()
