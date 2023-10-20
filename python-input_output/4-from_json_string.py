#!/usr/bin/python3
"""define function to return object from JSON"""


def from_json_string(my_str):
    """return object from JSON"""
    import json
    return json.loads(my_str)
