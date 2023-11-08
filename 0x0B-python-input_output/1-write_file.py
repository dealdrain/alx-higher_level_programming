#!/usr/bin/python3

"""Defines a file-writing function."""


def write_file(filename="", text=""):
    """Write a str to text file.

    Args:
        filename (str): file  name.
        text (str): text to write.
    Returns:
        num of chars
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
