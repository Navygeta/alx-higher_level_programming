#!/usr/bin/python3
"""
Representation of class Student that defines a student with attributes
first_name, last_name, age
"""


class student:
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

    def to_json(self):
        """
        Public method to retrieve a dict representation of student instance.
        """
        return self.__dict__
