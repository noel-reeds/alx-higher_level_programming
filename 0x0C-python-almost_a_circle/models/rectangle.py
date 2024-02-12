#!/usr/bin/python3
"""This is a Rectangle Module"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
    """retrieves width attribute"""
    @property
    def width(self):
        return self.__width

    """sets the width attribute"""
    @width.setter
    def width(self, value):
        self.__width = value

    """retrieves height attribute"""
    @property
    def height(self):
        return self.__height

    """sets the height attribute"""
    @height.setter
    def height(self, value):
        self.__height = value

    """retrives y attribute"""
    @property
    def y(self):
        return self.__y

    """sets y attribute"""
    @y.setter
    def y(self, value):
        self.__y = value

    """retrieves x attribute"""
    @property
    def x(self):
        return self.__x

    """validates x attributes"""
    @x.setter
    def x(self, value):
        self.__x = value
