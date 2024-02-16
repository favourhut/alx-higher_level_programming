#!/usr/bin/python3
"""
This module contains a function that returns the
first and last name

"""


def say_my_name(first_name, last_name=""):

    """
    This function woult make print My name is <first name> <last name>

    Args:
        first_name: Contiasn the first name of the person
        last_name: Contains the lst name of the person

    Return:
        My name is <first name> <last name>

    Raises:
    TypeError: If first name and last name are not strings
    """

    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')

    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    print(f'My name is {first_name} {last_name}')
