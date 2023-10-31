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

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Rectangle initialization

        Args:
            width (int): New rectangle width
            height(int): Ne reectangle height
        """
        Rectangle.number_of_instances += 1
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

    def area(self):
        """
        Calculates area of the rectangle

        Returns:
            int: Area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates perimeter of the rectangle

        Returns:
            int: Perimeter of the rectangle
        """
        if self.__width > 0 and self.__height > 0:
            return 2 * (self.__width + self.__height)
        else:
            return 0

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the biggest rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        else:
            return (rect_2)

    def __str__(self):
        """
        Representation of the rectangle using the character "#".

        Returns:
            str:String representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        result_str = ""
        for j in range(self.__height):
            result_str += str(self.print_symbol) * self.__width + "\n"

        return result_str.rstrip()

    def __repr__(self):
        """
        String representation of the rectangle for eval().

        Returns:
            str: String representation of the rectangle.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Prints a message for every deletion of a rectangle
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
