#!/usr/bin/python3
"""class LockedClass"""


class LockedClass:
    __slots__ = ["first_name"]

    def __setattr__(self, att, val):
        """setattr method"""
        if hasattr(self, att):
            super().__setattr__(att, val)
        elif att == "first_name":
            super().__setattr__(att, val)
        else:
            raise AttributeError("'LockedClass' object has no \
attribute '{}'".format(att))
