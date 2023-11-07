#!/usr/bin/python3
"""
Function that creates an Object from a “JSON file”:
"""

import json


def load_from_json_file(filename):
    """
    Loads a JSON file and returns the corresponding Python object.

    Parameters:
        filename (str): The name of the JSON file to be loaded.

    Returns:
        The Python object represented by the contents of the JSON file.
    """
    with open(filename) as file:
        return json.load(file)
