#!/usr/bin/python3
"""This code print the ancii alphabet, in lowercase.
ommits letter q and e
"""
for alphabet in range(97, 112):
    if (alphabet == 101) or (alphabet == 113):
        continue
    """continue ommits alphabet q and e"""
    print(chr(alphabet).format(), end='')
