import numpy as np

class Vector3D:
    def __init__(self, x: np.float64, y: np.float64, z: np.float64):
        self.data = np.array([x, y, z])

    @property
    def x(self):
        return self.data[0]

    @property
    def y(self):
        return self.data[1]

    @property
    def z(self):
        return self.data[2]

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __repr__(self):
        return f"Vector3D(x={self.x}, y={self.y}, z={self.z})"

    def __add__(self, other):
        if isinstance(other, Vector3D):
            return Vector3D(*(self.data + other.data))
        else:
            raise TypeError("Unsupported operand type for +")

    def __sub__(self, other):
        if isinstance(other, Vector3D):
            return Vector3D(*(self.data - other.data))
        else:
            raise TypeError("Unsupported operand type for -")

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector3D(*(self.data * other))
        elif isinstance(other, Vector3D):
            return Vector3D(*(self.data * other.data))
        else:
            raise TypeError("Unsupported operand type for *")

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Vector3D(*(self.data / other))
        else:
            raise TypeError("Unsupported operand type for /")

    def magnitude(self):
        return np.linalg.norm(self.data)

    def dot_product(self, other):
        if isinstance(other, Vector3D):
            return np.dot(self.data, other.data)
        else:
            raise TypeError("Unsupported operand type for dot product")
