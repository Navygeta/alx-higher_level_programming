#!/usr/bin/python3

"""
Script that removes all characters c and C from a string.
"""


def no_c(my_string):

    new_string = "".join(char for char in my_string if char.lower != 'c')
    return new_string
