#!/usr/bin/python3
"""define function to write string to text file"""


def write_file(filename="", text=""):
    """write string to text file"""
    with open(filename, 'w', encoding='utf-8') as file:
        chars_written = file.write(text)
        return chars_written
