#!/usr/bin/python3
"""define class Student"""


class Student:
    """Simple class containing student data."""

    def __init__(self, first_name, last_name, age):
        """initialize student instances."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return dictionary descript for JSON serialization"""

        ret_dict = {}
        if type(attrs) is list:
            for item in attrs:
                if type(item) is not str:
                    return self.__dict__
            for key in attrs:
                if key in self.__dict__:
                    ret_dict.update({key: self.__dict__[key]})
            return ret_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):

        for key in json:
            self.__dict__.update({key: json[key]})
