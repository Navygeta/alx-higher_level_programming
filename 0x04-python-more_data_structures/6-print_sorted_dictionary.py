#!/usr/bin/python3

"""
Function that prints a dictionary by ordered keys.
"""


def print_sorted_dictionary(a_dictionary):

    sorted_keys = sorted(a_dictionary.keys())

    for key in sorted_keys:
        dict_value = a_dictionary[key]
        print("{}: {}".format(key, dict_value))
