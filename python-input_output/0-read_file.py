#!/usr/bin/python3
"""define function to read text file and prints to stdout"""

def read_file(filename=""):
    """Read a text file and print to stdout"""
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
