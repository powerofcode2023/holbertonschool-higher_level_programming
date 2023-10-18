i#!/usr/bin/python3
"""define class BaseGeomtry"""


class BaseGeometry:
    """class with public instance method"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate integer"""
        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
