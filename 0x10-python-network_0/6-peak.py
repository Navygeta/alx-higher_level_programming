#!/usr/bin/python3
"""
function that finds a peak in a list of unsorted integers.
"""


def find_peak(lst):
    if not lst:
        return None

    return find_peak_recursive(lst, 0, len(lst) - 1)


def find_peak_recursive(lst, low, high):

    if low == high:
        return lst[low]

    mid = (low + high) // 2

    if lst[mid] < lst[mid + 1]:
        return find_peak_recursive(lst, mid + 1, high)
    else:
        return find_peak_recursive(lst, low, mid)
