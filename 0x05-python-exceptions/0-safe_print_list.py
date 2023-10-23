#!/usr/bin/python3

"""
Function that prints x elements of a list.
"""


def safe_print_list(my_list=[], x=0):

    elements = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            elements += 1
        except IndexError:
            break
        finally:
            print("")
    return elements
