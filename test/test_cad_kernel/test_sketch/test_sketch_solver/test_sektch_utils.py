import unittest
from pyCAD.cad_kernel.sketch.sketch_solver.sketch_utils import DependencyGraph
from pyCAD.cad_kernel.sketch.sketch_exceptions import SketchGeometryError
from pyCAD.cad_kernel.sketch.geometry2.base import GeomObject2DTestStub
from pyCAD.cad_kernel.sketch.geometry2.point import Point2D


class TestDependencyGraph(unittest.TestCase):
    def setUp(self):
        self.graph = DependencyGraph()

    def test_add_object_without_dependencies(self):
        item = GeomObject2DTestStub("Item")
        self.graph.add_object(item)
        self.assertTrue(self.graph.graph.has_node(item))

    def test_add_object_with_dependencies(self):
        item1 = GeomObject2DTestStub("Item1")
        item2 = GeomObject2DTestStub("Item2")
        item3 = GeomObject2DTestStub("Item3", dependencies=[item1, item2])

        self.graph.add_object(item3)

        self.assertTrue(self.graph.graph.has_node(item1))
        self.assertTrue(self.graph.graph.has_node(item2))
        self.assertTrue(self.graph.graph.has_node(item3))
        self.assertTrue(self.graph.graph.has_edge(item3, item1))
        self.assertTrue(self.graph.graph.has_edge(item3, item2))

    def test_can_delete_when_no_dependencies(self):
        item = GeomObject2DTestStub("Item")
        self.graph.add_object(item)

        result = self.graph.can_delete(item)
        self.assertTrue(result)

    def test_can_delete_when_dependents_exist(self):
        # e.g. if a point is part of a line it just can't be deleted for now
        item1 = GeomObject2DTestStub("Item1")
        item2 = GeomObject2DTestStub("Item2")
        item3 = GeomObject2DTestStub("Item3", dependencies=[item1, item2])

        self.graph.add_object(item3)

        result = self.graph.can_delete(item1)
        self.assertFalse(result)

    def test_delete_object(self):
        item = GeomObject2DTestStub("Item")
        self.graph.add_object(item)
        self.assertTrue(self.graph.graph.has_node(item))

        self.graph.delete_object(item)
        self.assertFalse(self.graph.graph.has_node(item))

    def test_delete_object_with_dependents(self):
        item1 = GeomObject2DTestStub("Item1")
        item2 = GeomObject2DTestStub("Item2")
        item3 = GeomObject2DTestStub("Item3", dependencies=[item1, item2])

        self.graph.add_object(item3)

        with self.assertRaises(SketchGeometryError):
            self.graph.delete_object(item1)

    def test_delete_object_with_dependencies(self):
        item1 = GeomObject2DTestStub("Item1")
        item2 = GeomObject2DTestStub("Item2")
        item3 = GeomObject2DTestStub("Item3", dependencies=[item1, item2])

        self.graph.add_object(item3)

        self.graph.delete_object(item3)
        self.assertFalse(self.graph.graph.has_node(item3))


    