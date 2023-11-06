#!/usr/bin/python3

"""Checks an obj for class or sub class"""


def is_kind_of_class(obj, a_class):
    """Checks an obj for same class

    Args:
            obj (Any): Object
            a_class (Any): Class type
    """
    return (isinstance(obj, a_class))
