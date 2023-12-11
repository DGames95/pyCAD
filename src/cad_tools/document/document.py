"""
start with an empty doc. The doc keeps all the items that make it up. you can have a view of a document.

there will be part document, sketch document and assembly document types with additional features

documents can contain documents e.g. part will need sketch

"""

import logging

    

class Document():
    def __init__(self, ):
        self.items = []
        self.dependencies = {}

    def add_item(self, item, dependencies):
        self.items.append(item)