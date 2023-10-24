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
    def __init__(self, size):
        """
        Initializes a new square instance with given size.

        Args:
            self: The instance of the square class.
            size: The size of each side of the square.
        """
        self.__size = size
