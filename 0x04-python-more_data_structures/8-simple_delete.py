#!/usr/bin/python3

"""
Function that deletes a key in a dictionary.
"""


def simple_delete(a_dictionary, key=""):

    if key in a_dictioanry:
        del a_dictionary[key]
