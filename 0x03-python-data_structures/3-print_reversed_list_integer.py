#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    m = (len(my_list) - 1)
    while m >= 0:
        print('{}'.format(my_list[m]))
        m = m - 1
