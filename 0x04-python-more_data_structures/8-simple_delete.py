#!/usr/bin/python3

"""
Function that deletes a key in a dictionary.
"""


def simple_delete(a_dictionary, key=""):

    if key not in a_dictioanry:
        pass
    else:
        del a_dictionary[key]

        return a_dictionary
