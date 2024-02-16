#!/usr/bin/python3

"""

This module has function that returna the sum of two integers

"""


def add_integer(a, b=98):

    """

    This function adds two numbers and returns the result.

    If only one argument is provided, it adds that argument to the default value of 98.

    Parameters:
    a (int or float): The first number.
    b (int or float, optional): The second number. Default is 98.

    Returns:
    int or float: The sum of the two numbers.

    Raises:
    TypeError: If either `a` or `b` is not an integer or float.

    """
    if  type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, flaot):
        raise TypeError('b must be an integer')

    a = int
    b = int

    return (a + b)
