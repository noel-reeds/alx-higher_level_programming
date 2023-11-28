#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
mod = abs(number) % 10
if mod > 5:
    print(f"Last digit of {number:d} is {mod:d} and is greater than 5")
if mod == 0:
    print(f"Last digit of {number:d} is {mod:d} and is 0")
if mod < 6 and mod != 0:
    print(f"Last digit of {number:d} is {mod:d} and is less than 6 and not 0")
