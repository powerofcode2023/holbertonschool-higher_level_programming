#!/usr/bin/python3
"""define Base class"""


import json


class Base:
    """manage id attribute for classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize to given id or
        increase class nb_objects and set as default id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""
        list_dicts = []
        if list_objs is not None:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
        json_str = Base.to_json_string(list_dicts)
        with open(cls.__name__ + ".json", 'w') as file:
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string."""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with set attributes"""
        if cls.__name__ == "Rectangle":
            dummy = cls(3, 4)
        else:
            dummy = cls(4)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances."""
        filename = cls.__name__ + ".json"
        list_instances = []

        try:
            with open(filename, 'r') as file:
                list_dictionaries = cls.from_json_string(file.read())
                for dictionary in list_dictionaries:
                    list_instances.append(cls.create(**dictionary))
        except FileNotFoundError:
            pass

        return list_instances
