#!/usr/bin/python3
"""Only sub class of"""


def inherits_from(obj, a_class):
    """ returns True if the object is an instance of a class that inherited
    or false otherwise"""
    return isinstance(obj, a_class) and type(obj) is not a_class
