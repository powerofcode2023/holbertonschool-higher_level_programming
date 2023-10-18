#!/usr/bin/python3
"""define class BaseGeomtry"""


class BaseGeometry:
    """class with public instance method"""
    def area(self):
        raise Exception("area() is not implemented")
