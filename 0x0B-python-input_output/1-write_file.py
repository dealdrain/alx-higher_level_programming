#!/usr/bin/python3

"""Define a text file with a line-counting func."""


def number_of_lines(filename=""):
    """Returns num of lines."""
    lines = 0
    with open(filename) as f:
        for line in f:
            lines += 1
    return lines
