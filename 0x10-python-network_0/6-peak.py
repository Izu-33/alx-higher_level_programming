#!/usr/bin/python3
"""Uses binary search to define a peak-finding algorithm"""


def find_peak(list_of_integers):
    """Returns a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): An unsorted list of ints.

    Returns:
        A peak from list_of_integers.
    """
    arr = list_of_integers
    if arr == []:
        return None

    n = len(arr)
    if n == 1:
        return arr[0]
    elif n == 2:
        return max(arr)

    mid = int(n / 2)
    peak = arr[mid]
    if peak > arr[mid - 1] and peak > arr[mid + 1]:
        return peak
    elif peak < arr[mid - 1]:
        return find_peak(arr[:mid])
    else:
        return find_peak(arr[mid + 1:])
