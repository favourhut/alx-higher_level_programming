#!/usr/bin/python3

"""Creating the base class"""


class Base:

    """private class attribute"""
    __nb_objects = 0

    """Class constructor"""
    def __init__(self, id=None):

        """assign id with argument value"""
        if id is not None:
            self.id = id

            """else incrementing"""
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
