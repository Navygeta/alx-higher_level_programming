#!/usr/bin/python3
"""
Module that defines Rectangle class theat inherits form class BaseGeometry.
"""
from __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class inheriting form Base geometry class
    """

    def __init__(self, width, height):
        """
        Initializes a new rectangle.

        Args:
            width (int): Width of the rectangler.
            height (int): Height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
