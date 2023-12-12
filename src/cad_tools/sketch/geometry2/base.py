from abc import ABC, abstractmethod


def GeomObject2D(ABC):

    @abstractmethod
    def decompose(self) -> tuple:
        # if item is composed return constituents and self, else self, for the sketch tree
        ...

    @abstractmethod
    def translate(self, dx, dy):
        ...