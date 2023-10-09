#!/usr/bin/python3

"""
Script to retrieve an element from a list.
"""


def element_at(my_list, idx):

    """
    Args:
        my_list (list): The input list.
        idx (int): The index of the element to retrieve.

    Returns:
        The element at the specified index or None if index is  out of range.
    """
    if idx < 0 or idx > len(my_list):
        return None
    else:
        return my_list[idx]
