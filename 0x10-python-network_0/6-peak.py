#!/usr/bin/python3
"""
function that finds a peak in a list of unsorted integers.
"""


def find_peak(nums):
    """
    Function that finds a peak in numbers.
    """

    if not nums:
        return None

    low, high = 0, len(nums)

    while low < high:
        middle = low + (high - low) // 2

        if (middle == 0 or nums[middle] >= nums[middle - 1]) and \
                (middle == len(nums) - 1 or nums[middle] >= nums[middle + 1]):
            return nums[middle]

        if middle > 0 and nums[middle] < nums[middle - 1]:
            high = middle
        else:
            low = middle + 1

    return None
