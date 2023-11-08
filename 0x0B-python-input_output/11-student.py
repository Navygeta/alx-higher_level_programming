#!/usr/bin/python3
"""
Representation of class Student that defines a student with attributes
first_name, last_name, age
"""


class Student:
    """
    Representation of class student

    Public instance attributes:
        first_name
        last_name
        age

    Public method:
        to_json(): Retrieves a dictionary representation of a Student instance.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialization of student class

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Public method to retrieve a dict representation of student instance.
        """

        if (type(attrs) == list and
                all(type(atr) == str for atr in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__

    def reload_from_json(self, json_data):
        """
        Replaces all attributes of the Student.

        Args:
            json_data (dict): The key/value pairs to replace attributes with.
        """
    for atr, val in json_data.items():
        setattr(self, atr, val)
