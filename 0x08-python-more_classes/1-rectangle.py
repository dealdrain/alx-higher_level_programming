#!/usr/bin/python3
"""
"Rectangle"  module.

"""


class Rectangle:
    def __init__(self, width=0, height=0):
        self._set_width(width)
        self._set_height(height)

    def _set_width(self, width):
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        self._width = width

    def _get_width(self):
        return self._width

    width = property(_get_width, _set_width)

    def _set_height(self, height):
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self._height = height

    def _get_height(self):
        return self._height

    height = property(_get_height, _set_height)
