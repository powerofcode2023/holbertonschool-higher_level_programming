#!/usr/bin/python3
"""define class Square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class for square  that inherit from BaseGeometry"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """return area"""
        return self.__size ** 2

    def __str__(self):
        """string representation of Square"""
        return '[Square] {}/{}'.format(self.__size, self.__size)
