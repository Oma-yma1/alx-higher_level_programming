#!/usr/bin/python3
"""Defines an empty class Square"""


class Square:
    """Defines an empty class Square"""
    def __init__(self, size=0):
        """initialize with size"""
        if not isinstance(size, int):
            raise TypeError("size mustbe an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    def area(self):
        """Return area of Square"""
        return self.__size ** 2
