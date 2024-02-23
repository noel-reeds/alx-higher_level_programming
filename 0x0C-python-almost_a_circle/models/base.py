#!/usr/bin/python3
"""Base module, defines methods/attrs for other classes"""


class Base:
    """This is a Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
