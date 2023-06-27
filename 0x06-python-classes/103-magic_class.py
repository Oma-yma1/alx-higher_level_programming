#!/usr/bin/python3
"""Defines an empty class Square"""
import math


class MagicClass:
    """Defines an empty class Square"""
    def __init__(self, radius):
        """Initialze with size"""
        self.__radius =0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        return 2 ** self.__radius * math.pi

    def circumference(self):
        return 2 * math.pi * self.__radius
