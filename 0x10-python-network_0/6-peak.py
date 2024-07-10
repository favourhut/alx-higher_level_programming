#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds a peak in list_of_integers"""

    if list_of_integers is None or list_of_integers == []:
        return None
    p = 0
    high = len(list_of_integers)
    midnum = ((high - p) // 2) + p
    midnum = int(midnum)
    if high == 1:
        return list_of_integers[0]
    if high == 2:
        return max(list_of_integers)
    if list_of_integers[midnum] >= list_of_integers[mid - 1] and\
            list_of_integers[mid] >= list_of_integers[midnum + 1]:
        return list_of_integers[midnum]
    if midnum > 0 and list_of_integers[mid] < list_of_integers[midnum + 1]:
        return find_peak(list_of_integers[midnum:])
    if midnum > 0 and list_of_integers[mid] < list_of_integers[midnum - 1]:
        return find_peak(list_of_integers[:midnum])
