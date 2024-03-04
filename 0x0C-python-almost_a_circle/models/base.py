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
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        elif not isinstance(list_dictionaries, list) or not \
                all(isinstance(var, dict) for var in list_dictionaries):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes JSON string to a file"""
        filename = f"{cls.__name__}.json"
        if list_objs is [] or list_objs is None:
            list_objs = []
            json_str = cls.to_json_string(list_objs)
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
        if json_string is None or json_string == "":
            return "[]"
        else:
            python_objs = json.loads(json_string)
            return python_objs

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes"""
        from models.square import Square
        dummy_obj = Square(5)
        dummy_obj.update(**dictionary)
        return dummy_obj

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = f"{cls.__name__}.json"
        if filename is None:
            return "[]"
        else:
            python_objs = cls.from_json_string(filename)
            for kwargs in python_objs:
                obj = cls.create(kwargs)
            return obj
