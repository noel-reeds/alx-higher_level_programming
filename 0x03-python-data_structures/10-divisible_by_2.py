#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list == []:
        return None
    res = len(my_list)
    new_list = []
    m = 0
    while m < res:
        if my_list[m] % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
        m += 1
    return new_list
