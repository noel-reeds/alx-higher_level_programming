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
        filename = f"{cls.__name__}.json"
        if list_objs == [] and list_objs == None:
            list_objs = []
            obj_dictionary = list_objs.to_dictionary()
            json_str = to_json_string(obj_dictionary)
            with open(filename, mode="w", encoding="utf-8") as MyFile:
                MyFile.write(json_str)
        else:
            list_dicts = []
            for obj in list_objs:
                obj_dictionary = obj.to_dictionary()
                list_dicts.append(obj_dictionary)
            json_str = cls.to_json_string(list_dicts)
            with open(filename, mode="w", encoding="utf-8") as MyFile:
                MyFile.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """JSON string to dictionary"""
        if json_string == None or json_string == ""
            return "[]"
        else:
            list_dictionaries = json.loads(json_string)
            return list_dictionaries
