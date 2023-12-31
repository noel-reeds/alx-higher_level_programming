#!/usr/bin/python3
def print_list_integer(my_list=[]):
    res = len(my_list)
    for m in range(res):
        print('{:d}'.format(my_list[m]))
