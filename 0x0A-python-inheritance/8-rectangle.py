#!/usr/bin/python3

"""Defines a class Rec from Base Geo."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rep rec."""

    def __init__(self, width, height):
        """Intialize  new Rectangle.

        Args:
            width (int): width of new Rec.
            height (int): height of new Rec.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
