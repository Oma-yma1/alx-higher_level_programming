#!/usr/bin/python3
"""write to a text file"""


def write_file(filename="", text=""):
    """return the number of chara written"""
    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
