#!/usr/bin/python3
"""
This is the "Square"  module.

This module provides a simple Square class with initialize size.
Defaults size to 0. Raise error on invalid size inputs.
Methods Getter and Setter properties for size.
Method area returns size of area of the square.
"""


class Square:
    def __init__(self, size=0):
        self._size = None
        self.size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        return self._size ** 2
