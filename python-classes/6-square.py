#!/usr/bin/python3
"""define square class"""


class Square:
    """define method of Square"""

    def __init__(self, size=0, position=(0, 0)):
        """size of the square"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (type(value) is not tuple or
                len(value) != 2 or
                all(isinstance(num, int) for num in value) or
                any(num < 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__position[1]):
                print()
            for i in range(0, self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
