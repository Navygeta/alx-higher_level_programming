#!/usr/bin/python3

"""
Function that divides element by element 2 lists.
"""


def list_division(my_list_1, my_list_2, list_length):

    nu_list = []
    for i in range(0, list_length):
        try:
            division = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            division = 0
        except ZeroDivisionError:
            print("division by 0")
            division = 0
        except IndexError:
            print("out of range")
            division = 0
        finally:
            nu_list.append(division)
    return nu_list
