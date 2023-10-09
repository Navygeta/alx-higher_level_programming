#!/usr/bin/python3

"""
Script that replaces an element in a list at a specific position
without modifying the original list.
"""


def new_in_list(my_list, idx, element):

    if idx < 0 or idx >= len(my_list):
        return my_list.copy()
    list_copy = my_list.copy()
    list_copy[idx] = element

    return list_copy
