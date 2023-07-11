#!/usr/bin/python3
"""save object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to text file using a JSON representation"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
