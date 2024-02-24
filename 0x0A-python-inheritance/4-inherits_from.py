#!/usr/bin/python3

"""

This function uses issubclass to check for 
an instanceof a class that inherited (directly or 
indiretly)
else return False

"""


def inherits_from(obj, a_class):

    """
    Returns True or False

    Args:
        obj: the object to check
        a_class: The class to check against

    Returns:
    True if the obj is an instance of a_class else False

    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
