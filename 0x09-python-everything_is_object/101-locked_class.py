#!/usr/bin/python3


class LockedClass:
    """Locked Class
    """
    __slots__ = ['first_name']


if __name__ == '__main__':
    lc = LockedClass()
    lc.first_name = "John"
    try:
        lc.last_name = "Snow"
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
