#!/usr/bin/python3

"""
Function that prints and integer.
"""


def safe_print_integer(value):

    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
