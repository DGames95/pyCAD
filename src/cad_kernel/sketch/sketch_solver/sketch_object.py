from enum import Enum
import logging

from ....app.pop_up_warning import PopUpWarning
from ...part.geometry3.plane import Plane3D
from ...part.geometry3.point import Point3D 
from ...part.geometry3.vector import Vector3D 
from geometry2.base import GeomObject2D
from geometry2.point import Point2D
from .sketch import Sketch
from .solver_utils import ConstraintGraph

class SketchObjectState(Enum):
    # this class manages the state of the sketch object
    # they are mutually exclusive
    # note, technically it can be edited and over/under constrained, but we do not know until we solve

    SOLVED = 0  # all green
    OVERCONSTRAINED = 1  # solver is applied but overconstrined
    UNDERCONSTRAINED = 2  # solver applied but underconstrained
    ERROR = 3  # solver applied but error
    SOLVING = 4  # if the object is currently being solved
    EDITED = 5  # if the object has been edited since the last solve (or no solve yet)
    

class SketchObject:
    # this class manages the "user interface" and the 3D position of this sketch
    def __init__(self, plane = Plane3D, logger = None):
        self.plane = Plane3D()
        self.origin = Point2D(0, 0)
        self.sketch = Sketch()
        self.sketch += self.origin

        self.state = SketchObjectState.EDITED
        self.logger = None

        self.pointer = 0  # this is the index of the current object

    @property
    def logger(self):
        # Try to fetch an existing logger if it exists
        if self._logger is not None:
            return self._logger
        else:
            # If a logger doesn't exist, create a dummy logger
            self._logger = logging.getLogger(__name__)
            self._logger.addHandler(logging.NullHandler())
            return self._logger

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
        if self.state == SketchObjectState.SOLVED:
            self.logger.info("Sketch object is already solved")
        elif self.state == SketchObjectState.SOLVING:
            self.logger.info("Sketch object is already solving")
        elif self.state == SketchObjectState.OVERCONSTRAINED:
            self.logger.info("Sketch object is overconstrained")
        elif self.state == SketchObjectState.UNDERCONSTRAINED:
            self.logger.info("Sketch object is underconstrained")
        elif self.state == SketchObjectState.ERROR:
            # TODO decide if this is more user interaction for the app rather than here?
            value = PopUpWarning("Sketch object is in error state, solve again?").get_input()