#!/usr/bin/python3

"""
Module: my_module

This module defines the Square class.
"""


class Square:

    """
    This class represents a square.

    Attributes:
        __size: The size of each side of the square.
    """
    def __init__(self, size=0):
        """
        Initializes a new square instance with given size.

        Args:
            self: The instance of the square class.
            size: The size of each side of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        elif size < 0:
            raise ValueError("Size must be >= 0")
        self.__size = size
