#!/usr/bin/python3
"""Base Module"""


class Base:
    """This is a Base class"""
    __nb_objects = 0

    """Initializes instance objects"""
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
