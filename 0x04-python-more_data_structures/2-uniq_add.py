#!/usr/bin/python3

"""
Function that adds all unique integers in a list (only once for each integer).
"""


def uniq_add(my_list=[]):

    uniq_list = list(set(my_list))
    sum_result = sum(map(lambda x: x, uniq_list))

    return sum_result
