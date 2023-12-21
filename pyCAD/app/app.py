# app manages documents
# documents for now are either part or sketch

class App():
    def __init__(self):
        self.documents = []

    @property
    def active_document(self):
        pass

    def new_part(self):
        pass

    def new_sketch(self):
        pass

    def load_part(self, path):
        pass

    def save_part(self, path):
        pass

    def load_sketch(self, path):
        pass

    def save_sketch(self, path):
        pass