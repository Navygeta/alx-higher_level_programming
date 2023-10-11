#!/usr/bin/python3

"""
Function that returns a set of all elements present in only one set.
"""


def only_diff_elements(set_1, set_2):

    all_present = set_1 ^ set_2

    return all_present
