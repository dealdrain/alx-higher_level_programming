#!/usr/bin/python3
"""Defines a base geo class BaseGeometry."""


class BaseGeometry:
    """Rep base."""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a par wiht int.

        Args:
            name (str): Par name.
            value (int): Par lookupe.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
