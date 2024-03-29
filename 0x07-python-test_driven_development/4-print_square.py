#!/usr/bin/python3


def print_square(size):
    """
    A function that prints square with the character #
    """

    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    elif isinstance(size, float):
        raise TypeError('size must be an integer')

    for i in range(size):
        print('#' * size)
