from point import Point2D
from vector import Vector2D
from base import GeomObject2D

class Line2D(GeomObject2D):
    """
    create a sketch line defined by 2 points
    
    """

    def __init__(self, start_point: Point2D, end_point: Point2D):
        self.start_point = start_point
        self.end_point = end_point

    def translate(self, dx, dy):
        # Move the line by adjusting the positions of its points
        self.start_point.x += dx
        self.start_point.y += dy
        self.end_point.x += dx
        self.end_point.y += dy

    def decompose(self) -> tuple:
        return (self, self.start_point, self.end_point)


def Line2DVectorFactory(start_point: Point2D, vector: Vector2D, magnitude: np.float64)
    """
    create a Line2D object with 
    """
    end_point = start_point