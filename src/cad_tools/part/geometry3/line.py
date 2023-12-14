from point import Point3D
from vector import Vector3D
from base import GeomObject3D  # Assuming you have a GeomObject3D base class

class Line3D(GeomObject3D):
    """
    Create a 3D line defined by 2 points.
    """

    def __init__(self, start_point: Point3D, end_point: Point3D):
        self.start_point = start_point
        self.end_point = end_point

    def translate(self, dx, dy, dz):
        # Move the line by adjusting the positions of its points
        self.start_point.translate(dx, dy, dz)
        self.end_point.translate(dx, dy, dz)

    def decompose(self) -> tuple:
        return (self, self.start_point, self.end_point)
