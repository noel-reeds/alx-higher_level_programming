#!/usr/bin/python3
def islower(c):
    """Returns True for lower case and False otherwise"""
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
