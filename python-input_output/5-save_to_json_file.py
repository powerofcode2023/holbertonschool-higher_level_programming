#!/usr/bin/python3
"""define function to write JSON representatin of an object to file"""


def save_to_json_file(my_obj, filename):
    """write JSON representation of an object to a file"""
    import json

    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
