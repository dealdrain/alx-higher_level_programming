#!/usr/bin/python3
"""Defines a base geo."""


class BaseGeometry:
    """Rep base geo."""

    def area(self):
        """Not deployed."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer.

        Args:
            name (str):name of par.
            value (int): lookup par
        Raises:
            TypeError: value not int.
            ValueError: value <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
