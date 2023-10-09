#!/usr/bin/python3

"""
Script that prints a matrix of integers.
"""


def print_matrix_integer(matrix=[[]]):

    for row in matrix:
        for numz in row:
            print("{:d}".format(numz), end=" " if numz != row[-1] else "")
        print()
