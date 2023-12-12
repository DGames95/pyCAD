import numpy as np

from .vector import Vector2D
from .base import GeomObject2D

class Point2D():
    def __init__(self, x: np.float64, y: np.float64):
        self._position = Vector2D(x, y)

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, new_position: Vector2D):
        self._position = Vector2D(x, y)

    def decompose(self):
        return (self)

    def translate(self, dx, dy):
        raise NotImplementedError

    @property
    def x(self):
        return self._position.x

    @property
    def y(self):
        return self._position.y  

    def __add__(self, other):
        """
        add ability to add a vector to a point to change it's position

        points cannot be added
        """
        if not isinstance(other, Vector2D):
            raise TypeError("only Vector2D can be added to points")

        self._position += other
        return self

    def __str__(self):
        return str(f"Point{self.position}")