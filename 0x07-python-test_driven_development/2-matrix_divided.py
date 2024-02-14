#!/usr/bin/python3
"""

This module defines a matrix division function

"""


def matrix_divided(matrix, div):
    """
    This function divides all element in a matrix by a divisor

    Args:
        matrix: Alist of list whic mambers can be float or int
        div: The number to divide with
    Rases:
        TypeError: If the matrix contains a non-numbers
        TypeError: If the matrix contains a rows of different sizes
        TypeError: if the divisor is not an int or float
        ZeroDivisionError: if the divisor is 0
    Returns:
        A divided new matrix
    """

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(fav, int) or isinstance(fav, float))
                    for fav in [digt for row in matrix for digt in row])):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
