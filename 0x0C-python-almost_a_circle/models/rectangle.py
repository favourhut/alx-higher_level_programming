#!/usr/bin/python3

""" A class Rectangle that inherits from Base"""


from models.base import Base


class Rectangle(Base):

    """creating a Class constructor"""

    def __init__(self, width, height, x=0, y=0, id=None):

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    '''Creating the getter and setter method'''
    @property
    def width(self):

        '''return a private instance value'''
        return self.__width

    @width.setter
    def width(self, value):

        '''Assigning a setter method'''

        if (type(value) is not (int)):
            '''validating attributes'''
            raise TypeError('width must be an integer')

        if value <= 0:
            '''validating attributes'''
            raise ValueError('width must be > 0')

        self.__width = value

    @property
    def height(self):

        """height"""
        return self.__height

    @height.setter
    def height(self, value):

        '''setter height'''
        if (type(value) is not (int)):
            '''validating attributes'''
            raise TypeError('height must be an integer')

        if value <= 0:
            '''validating attributes'''
            raise ValueError('height must be > 0')

        self.__height = value

    @property
    def x(self):

        """return x"""
        return self.__x

    @x.setter
    def x(self, value):

        '''Setting x'''
        if (type(value) is not (int)):
            '''validating attributes'''
            raise TypeError('x must be an integer')
        if value < 0:
            '''validating attributes'''
            raise ValueError('x must be >= 0')

        self.__x = value

    @property
    def y(self):
        """ retun prive instance y"""
        return self.__y

    @y.setter
    def y(self, value):

        '''Setting for y'''
        if (type(value) is not (int)):
            '''Validating inputs'''
            raise TypeError('y must be a integer')

        if value < 0:
            '''validating attributes'''
            raise ValueError('y must be >= 0')
        self.__y = value

    ''' adding the public method def area(self)'''
    def area(self):

        '''returns the aeea value of the
        class rec'''
        return (self.__width * self.__height)
    
    '''adding th display public method'''
    def display(self):
        
        """Print the Rectangle using the `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")