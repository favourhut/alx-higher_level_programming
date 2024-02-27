#!/usr/bin/python3

"""

Write a function that writes a string to a text file (UTF8) and
returns the number of characters written

"""

def write_file(filename="", text=""):

    """Using withi to make sure the file is auto closed"""

    with open(filename, 'w' encoding='UTF_8') as fileName:

        """Returning the number of test inputed"""
        fileName.write(text)
