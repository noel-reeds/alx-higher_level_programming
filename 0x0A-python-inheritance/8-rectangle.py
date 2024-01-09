#!/usr/bin/python3
"""Added a class Rectangle which inherits from BaseGeometry"""


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


"""Inherits from BaseGeometry"""
class Rectangle(BaseGeometry):
    """Rep. a rectangle which inherits from BaseGeometry"""

    def __init__(self, width, height):
        """dunder init method, initializes width and height
        
        Args:
            width(int): width of retcangle
            height(int): height of rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
