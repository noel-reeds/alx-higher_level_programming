#!/usr/bin/python3
def no_c(my_string):
    res_str = ""
    for m in my_string:
        if m != 'c' and m != 'C':
            res_str += m
    return res_str
