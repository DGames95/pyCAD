from ..exceptions import CADException

class PartException(CADException):
    pass

class PartAssemblyError(PartException):
    pass

class PartGeometryError(PartException):
    pass