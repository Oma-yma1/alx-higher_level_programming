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
            json_dic = {}
            for attr in attrs:
                if hasattr(self, attr):
                    json_dic[attr] =getattr(self, attr)
            return json_dic
