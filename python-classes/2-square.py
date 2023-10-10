#!/usr/bin/python3
''' class square '''


class Square:
    ''' define the square'''
    def __init__(self, size=0):
        """Initialize the square with a size."""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
