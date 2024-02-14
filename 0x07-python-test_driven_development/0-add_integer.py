#!/usr/bin/python3

"""

This module has function that returna the sum of two integers

"""


def add_integer(a, b=98):
    """
    checks for flaoat then convert to int
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('a must be an integer')
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')
    return (int(a) + int(b))
