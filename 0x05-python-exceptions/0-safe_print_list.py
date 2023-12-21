#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """prints elements of a list and raises an exception for out of index"""
    if my_list is not None:
        try:
            for i in range(x):
                print("{:d}".format(my_list[i]), end="")
            print()
        except IndexError:
            print('Index out of range')
