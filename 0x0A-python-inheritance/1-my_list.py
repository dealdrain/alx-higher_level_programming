#!/usr/bin/python3

"""A class def for MyList"""


class MyList(list):

    def print_sorted(self):
        list_sorted = sorted(self)
        print(list_sorted)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
