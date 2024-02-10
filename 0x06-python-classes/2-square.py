#!/usr/bin/python3

"""A Square attribute class"""


class Square:

    """module of class"""
    def __init__(self, size=0):

        """private attribute of size"""
        self.__size = size

        """checking that size is int"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

            """Less thanzero"""
        elif size < 0:
            raise ValueError("size must be >= 0")
