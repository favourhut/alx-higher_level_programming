#!/usr/bin/python3

"""return the current square area"""


class Square:
    """A class representing a square"""
    
    def __init__(self, size=0):
        
        """Initialize a Square instance with size validation.
        
        Args:
            size (int): The size of the square. Defaults to 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size
        
    def area(self):
        """Returns the current square area"""
        
        return self.__size**2