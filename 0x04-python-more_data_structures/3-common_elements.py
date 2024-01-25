#!/usr/bin/python3
def common_elements(set_1, set_2):

    A_set = set(set_1)
    B_set = set(set_2)
    C_set = A_set & B_set

    if C_set:
        return (C_set)
    else:
        pass
