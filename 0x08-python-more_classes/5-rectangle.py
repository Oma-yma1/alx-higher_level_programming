#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:
    """Define a Rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """Return perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Print the rectangle with the character #"""
        if self.width == 0 or self.height == 0:
            return ""
        return ((("#" * self.width) + "\n") * self.height)[:-1]

    def __repr__(self):
        """Recreate a new instance by using eval"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Print message when Rectangle is deleted"""
        print("Bye rectangle...")
