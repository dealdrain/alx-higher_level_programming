#!/usr/bin/python3

"""Define class"""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Ini Student.

        Args:
            first_name (str): first name
            last_name (str): last name
            age (int): age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get dict of Student."""
        return self.__dict__
