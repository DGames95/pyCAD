import numpy as np

import numpy as np

class Vector2D:
    # NOTE vector is not an object, point is an object
    def __init__(self, x: np.float64, y: np.float64):
        self.data = np.array([x, y])

    @property
    def x(self):
        # no setter, use np array to set it so we can use numpy functions
        return self.data[0]

    @property
    def y(self):
        return self.data[1]

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector2D(x={self.x}, y={self.y})"

    def __add__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(*(self.data + other.data))
        else:
            raise TypeError("Unsupported operand type for +")

    def __sub__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(*(self.data - other.data))
        else:
            raise TypeError("Unsupported operand type for -")

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector2D(*(self.data * other))
        elif isinstance(other, Vector2D):
            return Vector2D(*(self.data * other.data))
        else:
            raise TypeError("Unsupported operand type for *")

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Vector2D(*(self.data / other))
        else:
            raise TypeError("Unsupported operand type for /")

    def magnitude(self):
        return np.linalg.norm(self.data)

    def dot_product(self, other):
        if isinstance(other, Vector2D):
            return np.dot(self.data, other.data)
        else:
            raise TypeError("Unsupported operand type for dot product")

        


