#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        result = (-number) % 10
    elif result >= 0:
        result = number % 10
        print('{:d}'.format(result), end="")
        return result
