import numpy as np
from .vector import Vector3D  # Assuming this is the relative import path

class Point3D:
    def __init__(self, x: np.float64, y: np.float64, z: np.float64):
        self._position = Vector3D(x, y, z)

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, new_position: Vector3D):
        self._position = Vector3D(new_position.x, new_position.y, new_position.z)

    def decompose(self):
        return (self.x, self.y, self.z)

    def translate(self, dx, dy, dz):
        if not all(isinstance(val, (int, float)) for val in [dx, dy, dz]):
            raise TypeError("Translation values must be numbers")
        self._position += Vector3D(dx, dy, dz)

    @property
    def x(self):
        return self._position.x

    @property
    def y(self):
        return self._position.y

    @property
    def z(self):
        return self._position.z

    def __add__(self, other):
        if not isinstance(other, Vector3D):
            raise TypeError("Only Vector3D can be added to points")
        self._position += other
        return self

    def __str__(self):
        return f"Point3D{self.position}"
