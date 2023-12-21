from enum import Enum
import logging

from ...part.geometry3.base import GeomObject3D
from ...part.geometry3.plane import Plane3D
from ...part.geometry3.point import Point3D 
from ...part.geometry3.vector import Vector3D 
from ..sketch_exceptions import SketchGeometryError, SketchSolverError
from geometry2.base import GeomObject2D
from geometry2.point import Point2D
from geometry2.vector import Vector2D
from .sketch import Sketch
from .solver_utils import ConstraintGraph


class SketchObject(GeomObject3D):
    """
    basically a pointer to a Sketch
    
    """
    def __init__(self, plane: Plane3D):
        self.plane = plane
        self.sketch = Sketch()

        # add the origin and axes to the sketch, for easier addition of constraints
        self.origin = Point2D(0, 0)
        self.x_axis = Vector2D(1, 0)
        self.y_axis = Vector2D(0, 1)

        self.sketch += self.origin
        self.sketch += self.x_axis
        self.sketch += self.y_axis

    

    