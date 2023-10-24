#!/usr/bin/env python3

"""
This is a "Square"  module.
"""


class Square:
    """A class that defines a square by size and can compute area"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size
