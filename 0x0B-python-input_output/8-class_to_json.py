#!/usr/bin/python3
"""class to json"""


def class_to_json(obj):
    """returns the dictionary description with simple data"""
    return obj.__dict__
