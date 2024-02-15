#!/usr/bin/python3

"""

This module has function that returna the sum of two integers

"""


def add_integer(a, b=98):
    """
    checks for flaoat then convert to int
    """
    if type(a) != int and type(a) != float:
        raise TypeError('a must be an integer')
    if type(b) != int and type(b) != float:
        raise TypeError('b must be an integer')

    return (int(a) + int (b))
