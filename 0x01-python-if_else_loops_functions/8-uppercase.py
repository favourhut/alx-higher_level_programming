#!/usr/bin/python3
def uppercase(str):
    for letters in str:
        if 97 <= ord(letters) <= 122:
            storedLowerCase = letters - 32
            print({}.format(storedLowerCase))
        print({}.format(letters))
    