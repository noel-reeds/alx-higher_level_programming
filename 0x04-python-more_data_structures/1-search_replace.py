#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for m in range(len(my_list)):
        if my_list[m] == search:
            new_list[m] = replace
    return new_list
