from ..exceptions import CADException

class SketchException(CADException):
    pass

class SketchConstraintError(SketchException):
    pass

class SketchGeometryError(SketchException):
    pass

class SketchSolverError(SketchException):
    pass