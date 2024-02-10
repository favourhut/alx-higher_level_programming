#!/usr/bin/python3

"""A Square attribute class"""


class Square:

    """module of class"""
    def __init__(self, size=0):

        """private attribute of size"""
        self.__size = size

    """defining the getter and setter"""
    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):

        """checking that size is int"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

            """Less thanzero"""
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        return (self.__size * self.__size)
