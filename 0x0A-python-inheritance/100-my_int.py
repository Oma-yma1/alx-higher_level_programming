#!/usr/bin/python3
"""class myint"""


class MyInt(int):
    """class myint"""
    def __eq__(self, other):
        """equality"""
        return super().__ne__(other)

    def __ne__(self, other):
        """inequality"""
        return super().__eq__(other)
