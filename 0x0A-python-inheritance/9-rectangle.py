#!/usr/bin/python3
"""BaseGeometry module"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle"""
    def __init__(self, width, height):
        """instantiation"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """calculate the area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """return string representation"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
