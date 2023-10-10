#!/usr/bin/python3

"""
Function that finds all multiples of 2 in a list.
"""


def divisible_by_2(my_list=[]):

    return [numz % 2 == 0 for numz in my_list]
