#!/usr/bin/python3
"""This is an empty class"""


class BaseGeometry:
    """public instance method"""
    def area(self):
        raise Exception('area() is not implemented')

    """validates an integer"""
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        elif value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
        self.value = value
        self.name = name
