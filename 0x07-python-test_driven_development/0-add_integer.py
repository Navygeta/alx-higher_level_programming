#!/usr/bin/python3

"""
Module: Function that adds 2 integers
"""


def add_integer(a, b=98):
    """
    Adds 2 integers

    Args:
        a (int): First parameter of int type
        b (int): Second parameter of int type

    Raises:
        TypeError: If paramaeters are non int or float

    Return:
        Sum: The sum of the 2 parameters a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
