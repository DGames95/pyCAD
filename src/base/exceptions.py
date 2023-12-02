# plan as many exceptions as possible

class CADException(Exception):
    pass

class FileLoadError(CADException):
    def __init__(self, file_path):
        super().__init__(f"Error loading file: {file_path}")
        self.file_path = file_path


class NoAxesException(CADException):
    # raise if an item needs