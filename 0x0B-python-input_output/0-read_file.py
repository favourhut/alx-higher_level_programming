#!/usr/bin/python3

"""

Writing a function that reads a text filr and
prints it out to stdout

"""


def read_file(filename=""):
    with open(filename, encoding='UTF-8') as a_file:
        for line in a_file:
            print(line, end="")
