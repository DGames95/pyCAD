import numpy as np

from .vector import Vector2D
from .base import GeomObject2D

class Point2D():
    def __init__(self, x: np.float64, y: np.float64):
        self._position = Vector2D(x, y)

    @property
    def x(self):
        return self._position.x

    @property
    def y(self):
        return self._position.y  
    
    @x.setter
    def x(self, new_x: np.float64):
        raise AttributeError("x is a read only property. \
                             To change the position of a point, use the translate method, \
                              to edit directly, use the position_vector attribute")
    
    @y.setter
    def y(self, new_y: np.float64):
        raise AttributeError("y is a read only property. \
                             To change the position of a point, use the translate method, \
                              to edit directly, use the position_vector attribute")

    @property
    def position_vector(self) -> Vector2D:
        return self._position

    @position_vector.setter
    def position(self, new_position: Vector2D):
        self._position = new_position

    def dependencies(self):
        return None

    def translate(self, dx, dy):
        raise NotImplementedError
    
    def rotate(self, angle, center_point):
        raise NotImplementedError

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