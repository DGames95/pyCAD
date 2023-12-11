from ..base.part import Geometry
from ..base.document import Document

class Renderer():
    def __init__(self, document: Document):
        self.document = document
        self.vertices = []
        self.faces = []

    def render_obj(self):
        for item in self.document():
            if isinstance(item, Geometry):
                item.vertices = None