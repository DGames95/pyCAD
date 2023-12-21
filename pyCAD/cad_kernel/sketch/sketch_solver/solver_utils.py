# solver is an observer of geometry objects
from .constraints import Constraint
import networkx as nx

class ConstraintGraph:
    def __init__(self):
        self.graph = nx.Graph()

    def add_constraint(self, item1, item2, constraint):
        self.graph.add_edge(item1, item2, constraint=constraint)

    def delete_constraint(self, item1, item2):
        if self.graph.has_edge(item1, item2):
            self.graph.remove_edge(item1, item2)

    def delete_item(self, item):
        self.graph.remove_node(item)

    def get_constraints_between(self, item1, item2):
        return self.graph.get_edge_data(item1, item2)

    def display(self):
        print("Graph Edges:")
        for edge in self.graph.edges(data=True):
            print(f"{edge[0]} - {edge[1]}: {edge[2]['constraint']}")


class SolutionMatrix:
    def __init__(self):
        self.matrix = None

    def construct(self):
        """
        in order to create the matrix, we need to know all the primitives
        and we need to split them into their parameters
        """
        
        pass

    def update(self):
        pass

    def clear(self):
        pass