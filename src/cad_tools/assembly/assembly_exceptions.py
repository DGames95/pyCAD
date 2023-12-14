from ..exceptions import CADException

class AssemblyException(CADException):
    pass

class AssemblyConstraintError(AssemblyException):
    pass

class AssemblyInterferenceError(AssemblyException):
    pass
