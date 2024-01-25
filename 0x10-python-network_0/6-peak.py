#!/usr/bin/python3
"""
finding a peak
"""


def find_peak(list_of_integers):
    if not list_of_integers:
        return
    peak = list_of_integers[0]
    for num in list_of_integers:
        if peak < num:
            peak = num
    return peak
