#!/usr/bin/python3

"""Access and update private attribute"""


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
        return (self.__size**2)