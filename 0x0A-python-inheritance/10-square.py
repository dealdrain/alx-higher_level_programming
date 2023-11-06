#!/usr/bin/python3
"""Define Rec subclass sq."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Rep a sq."""

    def __init__(self, size):
        """Initialization.
        Args:
            size (int): new square size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
