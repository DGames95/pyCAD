import networkx as nx
from ..sketch_exceptions import SketchGeometryError
from ..geometry2.base import GeomObject2D

class DependencyGraph:
    def __init__(self):
        # use a directed graph where an item points to it's dependencies.
        self.graph = nx.DiGraph()

    def _add_node(self, item):
        """
        Add an item to the graph. 
        If the item has dependents, it will be connected to these dependents.

        :param item: The item to be added.
        :param dependents: A list of dependents of the item. Default is None.
        """
        # Add the item itself
        if not self.graph.has_node(item):
            self.graph.add_node(item)     

    def _add_dependencies(self, item, dependencies:list):
            for dependency in dependencies:    
                # now add the dependency to the graph (recursive!)
                self.add_object(dependency)

                # Create an edge from the item to its dependency
                self.graph.add_edge(item, dependency)

    def add_object(self, item: GeomObject2D):
        """
        Add an item to the graph. 
        If the item has dependents, it will be connected to these dependents.

        :param item: The item to be added.
        :param dependents: A list of dependents of the item. Default is None.
        """
        dependencies = item.dependencies()

        self._add_node(item)
        if dependencies is not None:
            self._add_dependencies(item, dependencies)

    def can_delete(self, obj):
        # In a directed graph, predecessors are the dependents
        # If there are no predecessors, the object can be deleted
        return not list(self.graph.predecessors(obj))

    def delete_object(self, obj):
        # for simplicity, deleting an object will NOT delete it's dependencies
        if self.can_delete(obj):
            self.graph.remove_node(obj)
        else:
            raise SketchGeometryError(f"Cannot delete {obj} as it has dependents")

    def display(self):
        print(self.graph.edges())

