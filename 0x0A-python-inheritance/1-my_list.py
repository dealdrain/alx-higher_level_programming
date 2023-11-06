#!/usr/bin/python3

"""class def for the List"""


class MyList(list):

    """List inherits from the class"""

    def print_sorted(self):
        """Sort the elements"""
        list_sorted = sorted(self)
        print(list_sorted)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
