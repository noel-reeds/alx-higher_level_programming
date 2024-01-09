#!/usr/bin/python3

"""Module checks for instance of a class, or a superclass"""


def is_kind_of_class(obj, a_class):
    """Return True for an instance, False otherwise"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
