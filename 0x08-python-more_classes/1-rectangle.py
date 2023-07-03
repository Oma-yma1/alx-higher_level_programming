#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:
    """Define a Rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize a Rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Retrieve the width of rectangle"""
        return self.width

    @width.setter
    def width(self, value):
        """set the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieve the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
