#!/usr/bin/python3
"""define Base class"""


class Base:
    """manage id attribute for classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize to given id or
        increase class nb_objects and set as default id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
