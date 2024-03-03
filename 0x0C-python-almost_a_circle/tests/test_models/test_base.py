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

    def test_width(self):

        rect = Rectangle(2, 3, 4, 5, -6)
        self.assertEqual(rect.id, -6)

if __name__ == '__main__':
    unittest.main()
