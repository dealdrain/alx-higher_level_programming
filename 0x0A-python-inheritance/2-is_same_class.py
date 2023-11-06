#!/usr/bin/python3
"""A func checking if an obj is from specific class"""


def is_same_class(obj, a_class):
    """Returning True if obj and class are same"""
    return type(obj) is a_class
