#!/usr/bin/python3
"""Create a Geometry Class"""


class BaseGeometry():
    """A Base Geo class"""

    def area(self):
        """Not deployed"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate int"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
