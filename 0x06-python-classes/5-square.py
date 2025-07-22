#!/usr/bin/python3

"""Modify: Adding a method that prints in 
stdout the square with the character #
"""


class Square:
    """A class representing a square"""
    
    def __init__(self, size=0):
        
        """Initialize a Square instance with size validation.
        
        Args:
            size (int): The size of the square. Defaults to 0.
        """
        self.__size = size
    
    @property   
    def size(self):
        """getter property to retrieve private size"""
        return (self.__size)
    
    @size.setter
    def size(self, value):
        """setter property set it"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        
    def area(self):
        """Returns the current square area"""
        return (self.__size) * (self.__size)
    
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for length in range(self.__size):
                for breadth in range(self.__size):
                    print("#", end"")
                print()
        self.__size = size
        