#!/usr/bin/env python3
# function that finds a peak in a list of unsorted integers.

def find_peak(list_of_integers):
    """returns the peak of list of unsorted integers"""
    n = len(list_of_integers)

    if n == 1:
        return list_of_integers[0]
    elif n == 2:
        return max(list_of_integers)

    mid = n // 2
    peak = list_of-integers[mid]
    if peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
        return peak
    elif peak < list_of_imtegers[mid - 1]:
        return find_peak([:mid])
    else:
        return find_peak([mid+1:])