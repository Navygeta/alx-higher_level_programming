#!/usr/bin/python3
"""
Function that returns true or false if obj is an instance of a class
"""


def is_same_class(obj, a_class):
    """
    Returns true or false if obj is an instance of a specified class

    Args:
        obj: The actual object to be checked
        a_class: Class in which object is being checked if it's an instance

    Return:
        True or false if obj is an instance of a class
    """
    if type(obj) == a_class:
        return True
    else:
        return False
