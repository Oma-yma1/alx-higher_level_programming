#!/usr/bin/python3
"""append to a  file"""


def append_write(filename="", text=""):
    """return the num of charachter added"""
    with open(filename, "a", encoding="UTF-8") as f:
        return f.write(text)
