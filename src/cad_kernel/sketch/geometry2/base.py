from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Iterable


class GeomObject2D(ABC):

    @abstractmethod
    def dependencies(self) -> Iterable[GeomObject2D] | None:
        # each object will return it's direct components as a list
        # decompose will be called on the dependents until None is returned
        # e.g. point -> {self:None}

        # Default implementation for leaf objects with no dependencies
        return None

    @abstractmethod
    def translate(self, dx, dy):
        ...


class GeomObject2DTestStub(GeomObject2D):
    def __init__(self, name, dependencies=None) -> None:
        # dummy init for testing, always override. This is not an example of how real objects will be created
        # by defining dependencies directly here we can create structures for testing purposes quickly
        self.data = name
        self._dependencies = dependencies

    def dependencies(self):
        return self._dependencies

    def translate(self, dx, dy):
        raise NotImplementedError