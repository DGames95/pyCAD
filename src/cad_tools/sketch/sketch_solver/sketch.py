import functools

from ..geometry2.base import GeomObject2D
from .solver_utils import ConstraintGraph
from .sketch_utils import DependencyGraph

class Sketch:
    def __init__(self):
        self.items = []  # GeomObject2D == this is flat structure including all sub-objects
        self._map_item_index = None  # GeomObject2D: index == this is recomputed from items if None, so set to none if list is edited

        self.dependencies = DependencyGraph()  # the actual tree
        self.constraints = ConstraintGraph 

    @property
    @functools.cache
    def index_map(self):
        if self._index_map is None:
            self._index_map = {item: index for index, item in enumerate(self._my_list)}
        return self._index_map
    
    @property
    def num_objects(self):
        return len(self.items)

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

    def __add__(self, other):
        if isinstance(other, GeomObject2D):
            self.add_sketch_object(other)
        else:
            raise TypeError("SketchTree can only add GeomObject2D")      
        
