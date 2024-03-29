#!/usr/bin/python3

'''Definng a class'''


class Square:

    '''Making the instances'''
    def __init__(self, size):

        self.__size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):

        '''checking for the size if int'''
        if not isinstance(value, int):
            raise TypeError('size must be an integer')

        elif value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    def area(self):
        return (self.__size * self.__size)

    '''Public instance that prints the area in #'''
    def my_print(self):
        for a in range(0, self.__size):
            [print('#', end='') for b in range(self.__size)]
            print('')

        if self.__size == 0:
            print()
