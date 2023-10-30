#!/usr/bin/python3
"""
"Add Integer"  module.

"""


def add_integer(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return int(a) + int(b)
    else:
        raise TypeError("Both arguments must be integers or floats")
