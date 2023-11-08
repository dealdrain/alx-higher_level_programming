#!/usr/bin/python3
"""Def text file func"""


def append_after(filename="", search_string="", new_string=""):
    """Insert a text after each line if str is present

    Args:
        filename (str): file name
        search_string (str): Lookup str
        new_string (str): str input
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
