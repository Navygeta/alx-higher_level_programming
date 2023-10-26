#!/usr/bin/python3

"""
Module: my_module

This module defines the Square class.
"""


class Node:
    """
    This class represents a node.

    Attributes:
        __size: The size of each side of the square.
        __position: The position of the square.
    """
    def __init__(self, data, next_node=None):
        """
        Initializes a new square instance with given size and position.

        Args:
            self: The instance of the square class.
            size (int): The size of each side of the square.
            position (tuple): Coordinates of the square.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter method to retrieve square size.

        Returns:
            int: The size of each side of the square.
        """
        return self.__size

    @data.setter
    def data(self, value):
        """
        Setter method to set square size.

        Args:
            value (int): The size to set.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Get the current position of the square.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method to set square position.

        Args:
            value (tuple): Coordinates of the square.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if not (isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """
    """
    def __init__(self):
    self.__head = None
