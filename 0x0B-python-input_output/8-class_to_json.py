#!/usr/bin/python3


def class_to_json(obj):
    """unique  class attributes to dictionary
    Args:
        obj (object): object to be rendered unique
    """
    return (obj.__dict__)
