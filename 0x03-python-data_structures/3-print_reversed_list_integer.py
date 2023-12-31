#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
        m = (len(my_list) - 1)
        while m >= 0:
            print('{:d}'.format(my_list[m]))
            m = m - 1
