#!/usr/bin/python3

"""
Script that prints a matrix of integers.
"""


def print_matrix_integer(matrix=[[]]):

    for row in matrix:
        for nums in row:
            print("{:d}".format(nums), end='' if nums != row[-1] else '')
        print()
