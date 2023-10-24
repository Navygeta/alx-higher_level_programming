#!/usr/bin/python3

"""
Function that divides 2 integers and prints the result.
"""


def safe_print_division(a, b):

    try:
        div_result = a / b
    except (TypeError, ZeroDivisionError):
        div_result = None
    finally:
        print("Inside result: {}".format(div_result))
    return division
