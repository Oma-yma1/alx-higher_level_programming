#!/usr/bin/python3
"""Defines an empty class Square"""


class Square:
    """Defines an empty class Square"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """function size"""
        return self.__size

    @size.setter
    def size(self, value):
        """functon size"""
        if not isinstance(value, (int, float)):
            raise TypeError("size mut be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """return area square"""
        return self.__size ** 2

    def __lt__(self, other):
        """less than operator"""
        return self.area() < other.area()

    def __le__(self, other):
        """less than or = operator"""
        return self.area() <= other.area()

    def __eq__(self, other):
        """equal operator"""
        return self.area() == other.area()

    def __ne__(self, other):
        """not equal operator"""
        return self.area() != other.area()

    def __gt__(self, other):
        """sup than operator"""
        return self.area() > other.area()

    def __ge__(self, other):
        """sup or = to operator"""
        return self.area() >= other.area()
