#!/usr/bin/python3
"""
Module: Function that prints a square with # char
"""


def print_square(size):
    """
    Function that prints a square with # char

    Argrs:
        size (int): Size of sqr (width & height)

    Raises:
        TypeError: If size is not type int
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size.is_integer() and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        [print("#", end="") for x in range(size)]
        print("")
