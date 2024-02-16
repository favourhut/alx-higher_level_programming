#!/usr/bin/python3

"""

THis module add two integer

"""


def add_integer(a, b=98):
    """
    Here is a brief documentation to use this func.

    Args:
        a (int/float): First number to sum
        b (int/flaot): Secound number to sum

    Return:
        Returns the sum of a and b

    Raises:
        TypeError: If input is not a float / int
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
         raise TypeError('a must be an integer')
    if ((not isinstance(b, int) and not isinstance(b, float))):
         raise TypeError('b must be an integer')
    return (int(a) + int(b))
