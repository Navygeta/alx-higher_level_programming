#!/usr/bin/python3

"""
Function that returns the weighted average of all integers tuple.
"""


def weight_average(my_list=[]):

    if not my_list:
        return 0

    score = sum(entry[0] * entry[1] for entry in my_list)
    weights = sum(entry[1] for entry in my_list)

    return score / weights
