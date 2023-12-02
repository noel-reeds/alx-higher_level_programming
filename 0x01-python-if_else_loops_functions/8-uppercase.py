#!/usr/bin/python3
def uppercase(str):
    res = ""
    for char in str:
        if 'a' <= char <= 'z':
            char = chr(ord(char) - 32)
        res += char
    print('{}'.format(res))
