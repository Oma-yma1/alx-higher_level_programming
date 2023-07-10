#!/usr/bin/python3
"""square module"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """square class"""
    def __init__(self, size):
        """initializingsquare"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """area square"""
        return self.__size ** 2
