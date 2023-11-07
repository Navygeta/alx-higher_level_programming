#!/usr/bin/python3
"""
Module that defines Rectangle class theat inherits form class BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
        super().__init__()
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Return the area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return the print() and str() representation of a Rectangle.
        """
        string = f"[{self.__class__.__name__}] {self.__width}/{self.__height}"
        return string
