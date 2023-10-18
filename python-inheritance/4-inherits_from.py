#!/usr/bin/python3
"""define function"""


def inherits_from(obj, a_class):
    """return true if object is an instance"""
    if type(obj) != a_class:
        return isinstance(obj, a_class)
    else:
        return False
