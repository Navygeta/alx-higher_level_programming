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
    if idx < 0 < len(my_list):
        return my_list[idx]
    else:
        return None
