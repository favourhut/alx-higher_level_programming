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

        """
        Public instance method that validates the value parameter.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """

        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))

        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
