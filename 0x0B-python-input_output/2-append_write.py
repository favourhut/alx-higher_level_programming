#!/usr/bin/python3

"""

Write a function that appends a string at the end of a text
file (UTF8) and returns the number of characters added

"""


def append_write(filename="", text=""):

    """Creating a new file"""
    with open(filename, 'a', encoding='UTF-8') as fileName:

        """returns the number of text added"""
        return fileName.write(text)
