"""
Document is the user side of the corresponding cad_kernel object.

Can be though of as the api between the user app and the cad_kernel.

"""

import logging
from typing import Protocol
import cad_kernel
    

class Document(Protocol):
    pass


class PartDocument(Document):
    def __init__(self):
        self.part = cad_kernel.Part()

    @property
    def tree(self):
        return self.part.tree

    def add_sketch(self, sketch):
        # we need to create a sketchobject, however, unlike a geomobject we want to 
        # create a new sketchDocument in the app that allows us to edit the sketch
        # the sketchobject is basically a pointer to the sketch
        pass

    def edit_sketch(self, sketch):
        pass

class SketchDocument(Document):
    def __init__(self):
        self.sketch = cad_kernel.Sketch()

    
    def add_geometry(self, geometry):
        pass

    def tools(self):
        # lists all the tools available
        pass

    
