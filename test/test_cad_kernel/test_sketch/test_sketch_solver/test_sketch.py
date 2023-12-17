import unittest
from CAD_python.src.cad_tools.sketch.sketch_solver import sketch_object
from src.cad_tools.sketch.geometry2.point import Point2D


class TestSketchTree(unittest.TestCase):

    def test_add_sketch_object(self):

        sketch_tree = sketch_object.SketchTree()

        point1 = Point2D(1.0, 2.0)
        sketch_tree.add_sketch_object(point1)

        self.assertEqual(sketch_tree.items[0], point1)

    def test_delete_sketch_object_negative_index(self):
        sketch_tree = sketch_object.SketchTree()
        point1 = Point2D(1.0, 2.0)
        sketch_tree.add_sketch_object(point1)

        sketch_tree.delete_sketch_object(-1)

        self.assertEqual(sketch_tree.items, {})

    def test_delete_sketch_object_empty(self):
        sketch_tree = sketch_object.SketchTree()
        sketch_tree.delete_sketch_object(-1)

        self.assertEqual(sketch_tree.items, {})

    def test_delete_sketch_object_out_of_bounds(self):
        sketch_tree = sketch_object.SketchTree()
        point1 = Point2D(1.0, 2.0)
        sketch_tree.add_sketch_object(point1)
        
        with self.assertRaises(IndexError):
            sketch_tree.delete_sketch_object(1)

