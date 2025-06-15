#!/usr/bin/python3
def print_last_digit(number):
    for a in number:
        if a == 0:
            return a
        else:
            result = a % 10
        return result
