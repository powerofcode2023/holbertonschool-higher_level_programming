#!/usr/bin/python3
"""define function that count number of lines read from file"""


def number_of_lines(filename=""):
    """Return the number of lines in a text file"""
    line_count = 0
    with open(filename, encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            line_count += 1
    return line_count
