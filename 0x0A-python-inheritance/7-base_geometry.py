#!/usr/bin/python3
"""
Module that defines class BaseGeometry.
"""


class BaseGeometry:
    """
    Base geometry class representation.
    """

    def area(self):
        """
        Raises:
            Not implemented:
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value as an integer greater than 0.

        Args:
            name (str): Name of the value parameter.
            value: The value parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or == 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
