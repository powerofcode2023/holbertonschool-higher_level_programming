#!/usr/bin/python3
"""define function to return dictionary description for JSON serialization"""


def class_to_json(obj):
    """return dictionary description for JSON serialization"""
    return obj.__dict__
