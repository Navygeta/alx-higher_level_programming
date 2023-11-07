#!/usr/bin/python3
"""
class MyInt that inherits from int and modifies the behavior of
equality operators.
"""


class MyInt(int):
    """
    Integer class that inverts the behavior of == and != operators.

    Attributes:
        value (int): The integer value.
    """

    def __eq__(self, value):
        """
        Overrides the == operator to implement != behavior.

        Args:
            value: The value to compare.

        Returns:
            bool: True if values are not equal, False otherwise.
        """
        return self.real != value

    def __ne__(self, value):
        """
        Overrides the != operator to implement == behavior.

        Args:
            value: The value to compare.

        Returns:
            bool: True if values are equal, False otherwise.
        """
        return self.real == value
