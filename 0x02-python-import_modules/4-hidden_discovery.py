#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    a = dir()
    for i in range(len(a)):
        if a[i][:2] != "__":
            print(":s".format(a[i]))
