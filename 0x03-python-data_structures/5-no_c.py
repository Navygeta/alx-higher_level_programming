#!/usr/bin/python3

"""
Script that removes all characters c and C from a string.
"""


def no_c(my_string):

    new_string = my_string.replace('c', '').replace('C', '')
    return new_string
