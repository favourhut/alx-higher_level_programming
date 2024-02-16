#!/usr/bin/python3

"""

THis module add two integer

"""


def add_integer(a, b=98):
    """
    Here is a brief documentation to use this func.

    Args:
        a: First number to add
        b: Secound number to add

    Return:
        The addtion of both numbers

    Raises:
        TypeError: a must must be an integer
        TypeError: b must be an integer
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError('a must be an integer')
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError('b must be an integer')
    return (int(a) + int(b))
