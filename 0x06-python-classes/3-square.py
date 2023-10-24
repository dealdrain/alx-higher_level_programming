#!/usr/bin/python3
"""
This is a "Square"  module.
"""


class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size


if __name__ == '__main__':
    my_square_1 = Square(3)
    print("Area:", my_square_1.area())

    try:
        print(my_square_1.size)
    except AttributeError as e:
        print(e)

    try:
        print(my_square_1.__size)
    except AttributeError as e:
        print(e)

    my_square_2 = Square(5)
    print("Area:", my_square_2.area())
