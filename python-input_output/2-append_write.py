#!/usr/bin/python3
"""define function to appends string to text file"""


def append_write(filename="", text=""):
    """append string to text file"""
    with open(filename, 'a', encoding='utf-8') as file:
        chars_written = file.write(text)
        return chars_written
