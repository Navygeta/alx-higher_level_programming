#!/usr/bin/python3
"""
Module: Function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix.

    Args:
        matrix (list): List of lists
        div (int or float): Number to divide

    Raises:
        TypeError: If not list of lists of integers
        TypeError: If not same size
        TypeError: If not int or float
        TypeError: If div == 0

    Return:
        New matrix
    """
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    row_size = len(matrix[0])
    if any(len(row) != row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    nu_mtrix = [[round(element / div, 2) for element in row] for row in matrix]

    return nu_mtrix
