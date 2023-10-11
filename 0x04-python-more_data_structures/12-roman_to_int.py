#!/usr/bin/python3

def roman_to_int(roman_string):
    roman_numerals = {
            'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1
    }

    num = 0
    last = 0

    for letter in roman_string:
        if letter in roman_numerals:
            value = roman_numerals[letter]
            if last == 0 or last >= value:
                num += value
            elif last < value:
                num += value - (last * 2)

            last = value

    return num
