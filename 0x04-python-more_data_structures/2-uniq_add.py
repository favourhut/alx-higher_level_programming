#!/usr/bin/python3
def uniq_add(my_list=[]):
    Addup = set(my_list)
    digit = 0
    for i in Addup:
        digit += i
    return (digit)
