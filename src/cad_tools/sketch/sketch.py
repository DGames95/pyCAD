from geometry2 import 

class SketchTree:
    def __init__(self):
        self.items = {}
        self.dependencies = {}
        self.size = 0  # this is the index

    def add_sketch_object(self, geom_object: GeomObj2D) -> None:
        decomp = geom_object.decompose()
        primary_item = decomp[0]
        primary_item_index = self.size
        surrent_item_dependencies = decomp[1:]

        for item in decomp:
            self.items[self.size] = item
            self.size += 1

        self.dependencies[primary_item_index] = current_item_dependencies

    def delete_sketch_object(self, index):
        pass

    def delete_latest_sketch_object(self):
        self.delete_sketch_object(-1)
        
        

    


class Sketch:
    def __init__(self):

        self.origin = Point(0, 0, 0)
        self.sketch_objects = [self.origin]