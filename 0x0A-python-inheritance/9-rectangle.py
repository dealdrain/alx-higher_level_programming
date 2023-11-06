#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry:

    """Base Geometry class """

    def area(self):
        """Area function """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer_validator function
        validates the value
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):

    """Class Rectangle"""

    def __init__(self, width, height):

        """Instantiation with width and height"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Area function
        Returns: The area of the rectangle
        """

        return self.__width * self.__height

    def __str__(self):
        """The function for use in print() and str()
        """

        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
