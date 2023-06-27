#!/usr/bin/python3
"""Defines an empty class Square"""


class Square:
    """Defines an empty class Square"""
    def __init__(self, size=0):
        """Initialize the size"""
        self.size = size

    @property
    def size(self):
        """value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set value size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """return area of Square"""
        return self.__size ** 2

    def my_print(self):
        """print square string"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
