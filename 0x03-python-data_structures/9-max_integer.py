#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    res = (len(my_list)) - 1
    m = 0
    if res == 0:
        num = my_list[m]
    else:
        if my_list[m] < my_list[m+1]:
            num = my_list[m+1]
        else:
            num = my_list[m]
        while m < res:
            if num < my_list[m+1]:
                num = my_list[m+1]
            else:
                num = num
            m = m + 1
        return num
