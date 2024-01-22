#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    arg_Len = len(argv)
    if arg_Len != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)

    a = int(argv[1])
    sign = argv[2]
    b = int(argv[3])

    if sign == '+':
        print(f'{a} {sign} {b} = {add(a, b)}')
    elif sign == '-':
        print(f'{a} {sign} {b} = {sub(a, b)}')
    elif sign == '*':
        print(f'{a} {sign} {b} = {sub(a, b)}')
    elif sign == '/':
        print(f'{a} {sign} {b} = {sub(a, b)}')
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
