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
            size (int): The size of each side of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method to retrieve square size.

        Returns:
            int: The size of each side of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set square size.

         Args:
            value (int): The size to set.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
