#!/usr/bin/python3
"""
Func that returns an object (Python data structure) represented by a JSON str
"""
import json


def from_json_string(my_str):
    """
    Function that returns the (python data struct) represented by a JSON str.

    Args:
        my_str: JSON The string to be converted to python object.

    Return:
        The Python object represented by the input JSON string.
    """
    return json.loads(my_str)
