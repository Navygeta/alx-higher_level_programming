#!/usr/bin/python3

"""
Module: My module

This module defines a simple rectangle class to represent a rectangle
"""


class Rectangle:

    """
    A class representing a rectangle.

    Attributes:
    Width (int): The width of the rectangle.
    Height (int): The height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Rectangle initialization

        Agrs:
            width (int): New rectangle width
            height(int): Ne reectangle height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter for the width attribute

        Returns:
            int: The rectangle width
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height attribute

        Returns:
            int: The rectangle height
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value