#!/usr/bin/python3
"""define function to return JSON representation of an object"""


def to_json_string(my_obj):
    """return JSON representation of an object"""
    import json
    return json.dumps(my_obj)
