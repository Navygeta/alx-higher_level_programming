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
        __position: The position of the square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new square instance with given size and position.

        Args:
            self: The instance of the square class.
            size (int): The size of each side of the square.
            position (tuple): Coordinates of the square.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Get the current position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method to set square position.

        Args:
            value (tuple): Coordinates of the square.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if not (isinstance(value, tuple) and len(value) == 2 and
                all(isinstance(num, int) for num in value) and
                all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints in stdout the square with char #
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size, end="")
                if i < self.__size - 1:
                    print("")
