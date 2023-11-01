#!/usr/bin/python3
"""
Module: Function that prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    Prints full name

    Args:
        first_name: First name to be printed
        last_name: Last name to be printed

    Raises:
        TypeError: If full name is not string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
