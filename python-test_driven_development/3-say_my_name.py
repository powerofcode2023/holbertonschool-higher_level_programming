#!/usr/bin/python3
"""
  Print My name is <first name> <last name>
  first_name and last_name must be string
  otherwise raise typeerror exception
"""


def say_my_name(first_name, last_name=""):
    """ validation first name """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    """ print """
    print("My name is {} {}".format(first_name, last_name))
