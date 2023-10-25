#!/usr/bin/python3
""" Module for the Square class """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class that inherits from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Class constructor """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Getter for size """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter for size """
        self.width = value
        self.height = value

    def __str__(self):
        """ String representation of the Square instance """
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width))
