#!/usr/bin/python3

"""
Function that deletes a key in a dictionary.
"""


def simple_delete(a_dictionary, key=""):

    if a_dictioanry.get(key) is not None:
        del a_dictionary[key]
