#!/usr/bin/python3
"""
This class is about a rectangle.
A rectangle is a four-sided shape with opp. sides equal..
"""


class Rectangle:
    """An init method to initialize attributes.."""
    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height	
    """retrives the private attribute, width.."""
    @property
    def width(self):
        return self.__width
    """sets the private attr. width"""
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value
    """retrieves the height attribute"""
    @property
    def height(self):
        return self.__height
    """sets the height attribute"""
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
