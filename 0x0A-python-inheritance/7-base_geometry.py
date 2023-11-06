#!/usr/bin/python3
"""Define a base geo."""


class BaseGeometry:
    """Rep base geo."""

    def area(self):
        """Not deployed."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a par int.
        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
