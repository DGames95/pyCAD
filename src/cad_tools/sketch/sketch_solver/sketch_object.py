from ...part.geometry3.plane import Plane3D
from ...part.geometry3.point import Point3D 
from ...part.geometry3.vector import Vector3D 
from geometry2.base import GeomObject2D
from geometry2.point import Point2D
from .sketch import Sketch
from .solver_utils import ConstraintGraph

class SketchObject:
    # this class manages the "user interface" and the 3D position of this sketch
    def __init__(self, plane = Plane3D):
        self.plane = Plane3D()

        self.origin = Point2D(0, 0)
        self.sketch = Sketch()
        self.sketch += self.origin

        self.pointer = 0  # this is the index of the current object

    # Tree methods
    def add_sketch_object(self, geom_object: GeomObject2D) -> None:
        self.sketch.add_sketch_object(geom_object)
        self.pointer += 1

    def delete_sketch_object(self, index):

        #TODO checks
        self.sketch_objects.delete_sketch_object(index)
        self.pointer -= 1

    def delete_current_sketch_object(self):
        self.delete_sketch_object(self.pointer)

    def delete_latest_sketch_object(self):
        self.delete_sketch_object(-1)

    # Constraint methods

    def update(self):
        # solve
        pass