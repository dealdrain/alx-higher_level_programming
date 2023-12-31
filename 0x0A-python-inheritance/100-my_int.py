#!/usr/bin/python3
"""Define a class MyInt from int."""


class MyInt(int):
    """num int ops == and !=."""

    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value
