#!/usr/bin/python3

"""
Function that returns a key with the biggest integer value.
"""


def best_score(a_dictionary):

    if not a_dictionary:
        return None

    big_val = max(a_dictionary, key=a_dictionary.get)
    return big_val
