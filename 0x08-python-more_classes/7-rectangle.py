#!/usr/bin/python3
"""
This class is about a rectangle.
A rectangle is a four-sided shape with opp. sides equal..
"""


class Rectangle:
    """public cls atrribute for num of instances.."""
    number_of_instances = 0
    print_symbol = "#"

    """An init method to initialize attributes.."""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1
        type(self).print_symbol = Rectangle.print_symbol
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
        self.__height = value
    """computes the area of a rectangle"""
    def area(self):
        area = self.__height * self.__width
        return area
    """computes the perimeter of a rectangle"""
    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            perimeter = 0
            return perimeter
        else:
            perimeter = 2 * (self.__height + self.__width)
            return perimeter
    """displays a rectangle of diff. symbols.."""
    def display_rectangle(self):
        if self.__height == 0 or self.__width == 0:
            return ""
        rectangle = ""
        for m in range(self.__height):
            for n in range(self.__width):
                rectangle += str(self.print_symbol)
            if m < self.__height - 1:
                rectangle += "\n"
        return rectangle
    """dunder method for an unofficial the str rep. of the obj.."""
    def __str__(self):
        return self.display_rectangle()
    """dunder method for an official str. rep. of an obj.."""
    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    """deletes an instance of a class.."""
    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
