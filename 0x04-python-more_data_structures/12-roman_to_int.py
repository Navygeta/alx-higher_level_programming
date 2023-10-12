#!/usr/bin/python3

"""
Function that converts Roman numeral to Integer
"""


def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    r_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    rom_chars = all(char.upper() in r_dict for char in roman_string)

    if not rom_chars:
        return None

    rom_value = map(lambda char: r_dict[char], reversed(roman_string.upper()))

    int_val = 0
    prev_val = 0

    for value in rom_value:
        if value < prev_val:
            int_val -= value
        else:
            int_val += value
        prev_val = value

    if not (0 < int_val < 4000):
        return None

    return int_val
