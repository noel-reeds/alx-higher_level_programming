#!/usr/bin/python3

"""Module checks for inheritance"""


def inherits_from(obj, a_class):
    """Return True for an instance, False otherwise"""
    if isinstance(obj, a_class) and not type(obj) is a_class:
        return True
    return False
