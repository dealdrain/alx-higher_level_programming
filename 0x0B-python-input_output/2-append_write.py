#!/usr/bin/python3
"""Define a file-appending func."""


def append_write(filename="", text=""):
    """Appends str to end of a UTF8 text file.

    Args:
        filename (str): name of file
        text (str): str to append
    Returns:
        num of chars
    """
    with open(filename, mode="a", encoding="utf-8") as fd:
        fd.write(text)
        return len(text)
