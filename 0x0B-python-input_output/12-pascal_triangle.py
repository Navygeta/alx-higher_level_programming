#!/usr/bin/python3
"""
Function that represents a concept that produces a triangular array of numbers.
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle

    Args:
        n (int): Number of rows in the triangle to generate.

    Return:
        Triangle or an empty list if n <= 0
    """
    triangle = []

    if n <= 0:
        return []

    for i in range(n):
        row = [1] * (i + 1)
        triangle.append(row)

        if i > 1:
            for j in range(1, i):
                triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]

    return triangle
