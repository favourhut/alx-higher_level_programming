#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    digit = number % -10
elif number >= 0:
    digit = number % 10

print(f'Last digit of {number} is {digit} and is', end=" ")
if digit > 5:
    print('grater than 5')
elif digit == 0:
    print('0')
else:
    print('less than 6 and not 0')
