#!/usr/bin/python3
"""add attribute"""


def add_attribute(obj, add_att, ad_value):
    """add new attribute"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, add_att, ad_value)
