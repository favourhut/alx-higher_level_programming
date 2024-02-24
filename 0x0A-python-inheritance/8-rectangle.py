#!/usr/bin/python3

"""

Creating an empty class

"""


class BaseGeometry:

    """
    creating a public instance method"""
    def area(self):
        raise Exception('area() is not implemented')

    """Instance method that validates value"""
    def integer_validator(self, name, value):

        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))

        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


class Rectangle(BaseGeometry):

    """instantiation with width and height"""

    def __init__(self, width, height):

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
