#!/usr/bin/python3

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    line = ""
    for char in text:
        line += char
        if char in ['.', '?', ':']:
            print(line.strip(), end="\n\n")
            line = ""
    if len(line) > 0:
        print(line.strip(), end="")
