#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    return [n % 2 == 0 for n in my_list]
