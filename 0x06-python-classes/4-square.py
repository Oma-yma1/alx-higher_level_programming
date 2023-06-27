#!/usr/bin/python3
"""Defines an empty class Square"""


class Square:
    """Defines an empty class Square"""
    def __init__(self, size=0):
        """Initialize Square"""
        self.__size = size
    @property
    def size(self):
        """size of Square"""
        return self.__size

    @size.setter
    def size(self, value):
        """set value into size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """return square area"""
        return self.__size ** 2
