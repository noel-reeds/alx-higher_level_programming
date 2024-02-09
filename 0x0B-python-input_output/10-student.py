#!/usr/bin/python3
"""Module, defines a Student Class"""


class Student:
    """Defines a Student class"""

    def __init__(self, first_name, last_name, age):
        """Initializes public instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if isinstance(attrs, list):
            return attrs
        return self.__dict__
