#!/usr/bin/python3
"""define function to create object from JSON representation from file"""


def load_from_json_file(filename):
    """create object from JSON representation in file"""
    import json

    with open(filename, encoding='utf-8') as file:
        return json.load(file)
