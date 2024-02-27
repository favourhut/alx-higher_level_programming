#!/usr/bin/python3

"""

Writing a function that reads a text filr and
prints it out to stdout

"""


def read_file(filename=""):

    """using with to automate the closing of the file"""
    with open(filename, encoding='UTF-8') as a_file:

        """looping through the file"""
        for line in a_file:

            """Printing the file out"""
            print(line, end="")
