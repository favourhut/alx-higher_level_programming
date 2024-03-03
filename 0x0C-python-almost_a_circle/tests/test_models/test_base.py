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

"""

***Priority
I am now testing for Recangle module

"""
class TestRectangle(unittest.TestCase): 

    '''
        Testing rectangle
    '''

    def setUp(self):
        '''
            Initializing instance with width and height
            parameters
        '''
        self.r = Rectangle(5, 10)

    def tearDown(self):
        '''
            Deleting created instance
        '''
        del self.r

    def test_width(self):
        '''
            Testing the Rectangle width getter
        '''
        self.assertEqual(5, self.r.width)

    def test_height(self):
        '''
            Testing the Rectangle height getter
        '''
        self.assertEqual(10, self.r.height)

    def test_x(self):
        '''
            Testing Rectangle x getter and setter
        '''

        self.r.x = 54
        self.assertEqual(54, self.r.x)
        self.assertEqual(0, self.r.y) 

if __name__ == '__main__':
    unittest.main()
