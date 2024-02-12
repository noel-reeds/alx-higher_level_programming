#!/usr/bin/python3
"""Base Module"""


class Base:
    """This is a Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.id = type(self).__nb_objects + 1
