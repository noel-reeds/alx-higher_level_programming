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

    @staticmethod
    def to_json_string(list_dictionaries):
        """dictionary rep of an instance to JSON string"""
        if list_dictionaries:
            json_str = json.dumps(list_dictionaries)
            return json_str
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """writes JSON string to a file"""
        if list_objs:
            list_dicts = []
            for obj in list_objs:
                obj_dictionary = obj.to_dictionary()
                list_dicts.append(obj_dictionary)
            json_str = cls.to_json_string(list_dicts)
            with open("Rectangle.json", mode="w", encoding="utf-8") as MyFile:
                MyFile.write(json_str)
        else:
            list_objs = []
            obj_dictionary = list_objs.to_dictionary()
            json_str = to_json_string(obj_dictionary)
            with open("Rectangle.json", mode="w", encoding="utf-8") as MyFile:
                MyFile.write(json_str)
