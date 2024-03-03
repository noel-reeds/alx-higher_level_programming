#!/usr/bin/python3
"""Base module, defines methods/attrs for other classes"""
import json


class Base:
    """This is a Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    def to_json_string(list_dictionaries):
        """dictionary rep of an instance to JSON string"""
        if list_dictionaries:
            json_str = json.dumps(list_dictionaries)
            return json_str
        else:
            return "[]"
