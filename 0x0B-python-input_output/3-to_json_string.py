#!/usr/bin/python3
"""
Function that returns the JSON representation of an object (string).
"""
import json


def to_json_string(my_obj):
    """
    Function that returns the JSON representation of a given object.

    Args:
        my_obj: The object to be converted to a JSON string.

    Return:
    The JSON representation of an object (string).
    """
    return json.dumps(my_obj)
