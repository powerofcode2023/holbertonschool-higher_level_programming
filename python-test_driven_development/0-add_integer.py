#!/usr/bin/python3

"""
This module provides a function to add two integers.
"""


def add_integer(a, b=98):
    """
    Adds two numbers and returns the result.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
