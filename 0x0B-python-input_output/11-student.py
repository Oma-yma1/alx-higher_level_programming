#!/usr/bin/python3
"""student to json"""


class Student:
    """class student"""
    def __init__(self, first_name, last_name, age):
        """initialize instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation"""
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs
                    if hasattar(self, attr)}

        def reload_from_json(self, json):
            """reload json"""
            for le, va in json.items():
                setattr(self, ke, va)
