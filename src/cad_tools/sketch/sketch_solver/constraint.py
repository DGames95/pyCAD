"""
step 1: figure out if we are correctly constrained or not
step 2: figure out a "control error"
step 3: move the geometry to minimize the error

one point makes sense: how to do for 2 points


constraints:

every constraint stores SketchObjects that have been constrained

"""
from enum import Enum

class ConstraintType(Enum):
    COINCIDENCE = 1

class Constraint:
    def __init__(self, constraint_type, first: int, second: int, third: int):
        self.constraint_type = constraint_type
        self.first = first
        self.second = second
        self.third = third

    
