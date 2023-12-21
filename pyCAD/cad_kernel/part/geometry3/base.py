from abc import ABC, abstractmethod


class GeomObject3D(ABC):

    @abstractmethod
    def decompose(self) -> tuple:
        # if item is composed return self and constituents, else self, for the sketch tree
        ...

    @abstractmethod
    def translate(self, dx, dy, dz):
        ...