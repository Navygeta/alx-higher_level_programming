#!/usr/bin/python3
"""
Function that returns the dictionary description with simple data structure
(list, dictionary, string, integer and boolean) for JSON serialization
of an object.
"""


def class_to_json(obj):
    """
    Args:
        obj: An instance of a class with representable attributes.

    Return:
        A dictionary representing the object for serializationt.
    """
    return obj.__dict__
