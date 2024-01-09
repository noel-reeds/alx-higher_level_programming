#!/usr/bin/python3
""""This module checks for instantiation"""


def is_same_class(obj, a_class):
    """returns True for an instance and False otherwise"""
    if type(obj) is a_class:
        return True
    return False
