#!/usr/bin/python3

"""Func looking up methods of an obj"""


def lookup(obj):
    """Check availabble  methos
    Arguments: obj to be checked
    Return:  list
    """
    return dir(obj)
