#!/usr/bin/python3
def fizzbuzz():
    """Prints the numbers from 1 to 100 separated by a space"""
    for m in range(1, 101):
        if m % 3 == 0:
            print('{}'.format('Fizz'), end=' ')
        elif m % 5 == 0:
            print('{}'.format('Buzz'), end=' ')
        else:
            print('{}'.format(m), end=' ')
