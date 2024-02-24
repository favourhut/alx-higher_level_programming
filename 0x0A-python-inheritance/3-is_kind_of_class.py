#!/usr/bin/python3

"""

This function checks fir smae class or inherit from same class

"""


def is_kind_of_class(obj, a_class):

    """ This returns True if the object is an isntance of a class or 
    inherited from the class
    else returns False
    """
    return (isinstance(obj, a_class))
