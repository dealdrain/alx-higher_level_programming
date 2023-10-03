#!/usr/bin/python3

def print_last_digit(number):
    lasdig = int(str(number)[-1])
    print("{}".format(lasdig), end="")
    return lasdig
