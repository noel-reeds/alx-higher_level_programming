#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for m in range(len(my_list)):
        if my_list[m] == search:
            my_list[:]
            my_list[m] = replace
            new_list = my_list
    return new_list
