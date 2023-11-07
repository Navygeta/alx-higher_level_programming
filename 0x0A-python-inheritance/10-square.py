#!/usr/bin/python3
"""
Module that defines Square class theat inherits form class Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class inheriting form Rectangle class
    """

    def __init__(self, size):
        """
        Initializes a new square.

        Args:
            size (int): Square size.
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    @property
    def size(self):
        """
        Getter for the size attribute.

        Returns:
            int: The size of the square.
        """
        return self.__size

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
