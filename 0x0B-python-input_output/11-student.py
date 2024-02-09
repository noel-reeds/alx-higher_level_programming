#!/usr/bin/python3
"""
Module, defines a Student Class
"""


class Student:
    """
    Defines a Student class
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes public instance attributes
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance
        """
        if isinstance(attrs, list):
            for key in self.__dict__.copy():
                if key not in attrs:
                    self.__dict__.pop(key)
            return self.__dict__
        else:
            return self.__dict__
    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance
        """
        json = self.__dict__
        return json
