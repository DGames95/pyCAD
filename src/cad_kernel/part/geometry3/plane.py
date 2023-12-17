from point import Point3D
from vector import Vector3D
from base import GeomObject3D  # Assuming you have a GeomObject3D base class

class Plane3D(GeomObject3D):
    """
    Create a 3D plane defined by a point on the plane and a normal vector.
    """

    def __init__(self, point_on_plane: Point3D, normal_vector: Vector3D):
        self.point_on_plane = point_on_plane
        self.normal_vector = normal_vector

    def translate(self, dx, dy, dz):
        # Move the point on the plane
        self.point_on_plane.translate(dx, dy, dz)

    def decompose(self) -> tuple:
        return (self, self.point_on_plane, self.normal_vector)
