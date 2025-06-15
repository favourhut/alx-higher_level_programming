#!/usr/bin/python3
def uppercase(str):
    for letters in str:
        if 97 <= ord(letters) <= 122:
            upperCase = chr(ord(letters) - 32)
            print('{}'.format(upperCase))
        print()
