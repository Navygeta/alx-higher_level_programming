#!/usr/bin/python3
"""
Function that writes an Object to a text file, using a JSON representation
"""
import json


def save_to_json_file(my_bj, filename):
    """
    Function that writes an Object to a text file, using a JSON representation

    Args:
        my_obj: Object to serialize and save to file.
        filname (str): File where the JSON representation will be saved.
    """
    with open(filename, "w") as file:
        json.dump(my_obj, f)
