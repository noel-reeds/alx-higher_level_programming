#!/usr/bin/python3
"""creates a dict from a Python object"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure"""
    return obj.__dict__
    
