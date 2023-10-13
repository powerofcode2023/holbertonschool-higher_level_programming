#!/usr/bin/python3
"""8-rectangle.py:
    print a rectangle
"""


class Rectangle:
    """class Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Parameters
        ----------
        size : int
            the size of the rectangle.
        """
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        return (str(self.print_symbol) * self.__width + "\n") *\
            (self.__height - 1) + str(self.print_symbol) * self.__width

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__height, self.__width)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area < rect_2.area:
            return rect_2
        if rect_1.area > rect_2.area:
            return rect_1
        if rect_1.area == rect_2.area:
            return rect_1
