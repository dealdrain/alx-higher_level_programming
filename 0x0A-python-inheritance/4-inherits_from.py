#!/usr/bin/python3


def inherits_from(obj, a_class):
"""Checks for obj if an instance is inherited
    Args:
        obj (object): object
        a_class (class): class to lookup
    Returns:
        True if obj is instance or inherited from class, else False
"""
    if (type(obj) != a_class):
        return issubclass(type(obj), a_class)
    return False
