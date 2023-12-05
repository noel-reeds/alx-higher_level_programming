#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == "":
        return None
    for m in range(len(my_list) - 1):
        if my_list[m] > my_list[m+1]:
            return mylist[m]
        else:
            return my_list[m+1]
