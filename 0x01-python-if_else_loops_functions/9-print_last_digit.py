#!/usr/bin/python3
def print_last_digit(number):
    """Prints the last digit of a number"""
    if number < 0:
        res = -(abs(number % 10))
    else:
        res = number % 10
    return res
