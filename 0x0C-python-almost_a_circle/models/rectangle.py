#!/usr/bin/python3
"""This is a Rectangle Module"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes instances"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """retrieves width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width attribute"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """retrieves height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height attribute"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def y(self):
        """retrives y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets y attribute"""
        if type(value) is not int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    @property
    def x(self):
        """retrieves x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """validates x attributes"""
        if type(value) is not int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    def area(self):
        """returns the area value"""
        area = self.__height * self.__width
        return area

    def display(self):
        """prints a rectangle of '#' to stdout"""
        for var2 in range(self.__y):
            print()
        for var in range(self.__height):
            for var3 in range(self.__x):
                print(" ", end="")
            for var1 in range(self.__width):
                print('#', end="")
            print()

    def __str__(self):
        """overrides the __str__ method"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}"

    def update(self, *args):
        """assigns an argument to each attribute"""
        attrs = ["id", "width", "height", "x", "y"]
        object_dict = self.__dict__.copy()
        for index, value in enumerate(args):
            setattr(self, attrs[index], args[index])
