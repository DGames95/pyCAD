import functools
import logging
from enum import Enum

from ..sketch_exceptions import SketchGeometryError, SketchSolverError

from ..geometry2.base import GeomObject2D
from .solver_utils import ConstraintGraph
from .sketch_utils import DependencyGraph

class SketchState(Enum):
    # this class manages the state of the sketch object
    # they are mutually exclusive
    # note, technically it can be edited and over/under constrained, but we do not know until we solve

    SOLVED = 0  # all green
    OVERCONSTRAINED = 1  # solver is applied but overconstrined
    UNDERCONSTRAINED = 2  # solver applied but underconstrained
    ERROR = 3  # solver applied but error
    SOLVING = 4  # if the object is currently being solved
    EDITED = 5  # if the object has been edited since the last solve (or no solve yet)
    LOADING_SKETCH = 6  # if the object is currently loading a sketch file
    

class Sketch:
    def __init__(self, logger):
        self.items = []  # GeomObject2D == this is flat structure including all sub-objects
        self._map_item_index = None  # GeomObject2D: index == this is recomputed from items if None, so set to none if list is edited

        self.dependencies = DependencyGraph()  # the actual tree
        self.constraints = ConstraintGraph 

        self.state = SketchState.EDITED
        self.logger = logger

    @property
    @functools.cache
    def index_map(self):
        if self._index_map is None:
            self._index_map = {item: index for index, item in enumerate(self._my_list)}
        return self._index_map
    
    @property
    def num_objects(self):
        return len(self.items)

    def is_busy(self):
        return self.state == SketchState.SOLVING or self.state == SketchState.LOADING_SKETCH
    
    def is_solved(self):
        return self.state == SketchState.SOLVED

    def add_sketch_object(self, geom_object: GeomObject2D) -> None:
        self.insert_sketch_object(self.size, geom_object)

    def insert_sketch_object(self, index, geom_object: GeomObject2D) -> None:
        object_tree = geom_object.decompose()
        # items = {self:{depend1:{depend2:None}}} the objects
        # items = {self:None} the leaf objects

        # dependencies and constraints will be tracked by index
        for obj in object_tree:
            self.items.insert(index, geom_object)

    def delete_sketch_object(self, index):
        pass

    def delete_latest_sketch_object(self):
        self.delete_sketch_object(-1)

    def update(self):
        if self.state == SketchState.SOLVED:
            self.logger.info("Sketch object is already solved")
        elif self.state == SketchState.SOLVING:
            self.logger.info("Sketch object is already solving")
        elif self.state == SketchState.OVERCONSTRAINED:
            self.logger.info("Sketch object is overconstrained")
        elif self.state == SketchState.UNDERCONSTRAINED:
            self.logger.info("Sketch object is underconstrained")
        elif self.state == SketchState.ERROR:
            raise SketchSolverError("Sketch Object has unresolved errors")
        elif self.state == SketchState.EDITED:
            self.logger.debug("solving sketch %s", str(self.sketch))

    def load_sketch(self, file):
        pass

    def save_sketch(self, file):
        pass

    def __add__(self, other):
        if isinstance(other, GeomObject2D):
            self.add_sketch_object(other)
        else:
            raise TypeError("SketchTree can only add GeomObject2D")      
        
