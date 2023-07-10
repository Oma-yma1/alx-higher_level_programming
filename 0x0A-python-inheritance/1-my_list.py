#!/usr/bin/python3
"""Mylist class"""


class MyList(list):
    """MyList class"""
    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
