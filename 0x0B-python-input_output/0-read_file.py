#!/usr/bin/python3
"""Read text file"""


def read_file(filename=""):
    """Read a text file and print it"""
    with open(filename, 'r') as f:
        print(f.read(), end='')


if __name__ == "__main__":
    read_file()
