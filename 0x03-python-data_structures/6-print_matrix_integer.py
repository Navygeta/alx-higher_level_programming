#!/usr/bin/python3

"""
Script that prints a matrix of integers.
"""


def print_matrix_integer(matrix=[[]]):

    for row in matrix:
        for num in row:
            print("{:d}".format(num), end='')
        print()
