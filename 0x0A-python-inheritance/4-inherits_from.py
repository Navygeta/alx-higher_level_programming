#!/usr/bin/python3
"""
This module provides utility functions for class and inheritance checks.
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False.

    Args:
        obj: Object to be checked.
        a_class: The class to match the type of obj to.
    Returns:
        If obj is an inherited instance of a_class - True.
        Otherwise - False.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class:
