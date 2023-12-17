from math import sqrt

class Position():
    def __init__(self, x: float, y: float, z: float) -> None:
        self.vector = Vector(x, y, z)

class Vector():
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z

    @property
    def magnitude(self):
        pass

    @staticmethod
    def normalize(x, y, z):
        length = sqrt((x**2 + y ** 2 + z ** 2))
        return None
    
    def cross(self, other):
        pass

    def dot(self, other):
        pass

    def __mul__(self, other):
        self.dot(other)

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __div__(self, other):
        pass
    

