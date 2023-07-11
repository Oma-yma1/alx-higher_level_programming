#!/usr/bin/python3
"""search and update"""


def append_after(filename="", search_string="", new_string=""):
    """append after"""
    with open(filename, "r") as f:
        tex = f.readlines()

    with open(filename, "w") as f:
        for i in tex:
            f.write(i)
            if search_string in i:
                f.write(new_string)
