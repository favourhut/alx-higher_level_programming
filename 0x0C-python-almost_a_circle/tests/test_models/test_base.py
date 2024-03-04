#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import Rectangle


"""Creating a unittest for the Base module"""


class TestBase(unittest.TestCase):

    """Testing base"""

    def test_id_none(self):

        """testing a none valid id"""

        b = Base()
        self.assertEqual(1, b.id)

    def test_id(self):

        """tesing a valid id"""

        b = Base(20)
        self.assertEqual(20, b.id)

    def test_id_zero(self):

        """tesign when id is 0"""

        b = Base(0)
        self.assertEqual(0, b.id)

    def test_id_negative(self):

        """tesing when id is negative"""

        b = Base(-4)
        self.assertEqual(-4, b.id)

"""I am now testing for Recangle module"""



class TestRectangle(unittest.TestCase):
    
    '''Creating test files for the module Rectanlge'''
    
    def test_constructor(self):
        rectangle = Rectangle(10, 20, 5, 10, 1)
        self.assertEqual(rectangle.width, 10)
        self.assertEqual(rectangle.height, 20)
        self.assertEqual(rectangle.x, 5)
        self.assertEqual(rectangle.y, 10)
        self.assertEqual(rectangle.id, 1)

    def test_width_setter(self):
        rectangle = Rectangle(10, 20)
        rectangle.width = 15
        self.assertEqual(rectangle.width, 15)

    def test_height_setter(self):
        rectangle = Rectangle(10, 20)
        rectangle.height = 25
        self.assertEqual(rectangle.height, 25)

    def test_x_setter(self):
        rectangle = Rectangle(10, 20)
        rectangle.x = 5
        self.assertEqual(rectangle.x, 5)

    def test_y_setter(self):
        rectangle = Rectangle(10, 20)
        rectangle.y = 10
        self.assertEqual(rectangle.y, 10)
        
if __name__ == '__main__':
    unittest.main()
    