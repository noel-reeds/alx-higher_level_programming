#!/usr/bin/python3
"""
This is a class representing a square
"""


class Square:
    """
    The __init__ method is the constructor for the class
    Logic for the method will be added later.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Args:
            size(int): The size of the obj. square.
            position(tuple): cordinates of obj. square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
            self.__position = position

    """
    This is the area method of the class Square.
    Area is computed by size * size or size-squared
    """
    def area(self):

        area = self.__size ** 2  #: Area computation..size-squared.
        return area

    """
    Retrieves the size of the obj. square
    """
    @property
    def size(self):
        return self.__size

    """
    Sets or modifies the the size of the obj. with a new value.
    """
    @size.setter
    def size(self, value):

        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """
    A public instance method to print an obj. square to the
    standard out(stdout).
    """
    def my_print(self):

        if self.__size == 0:
            print()
        else:
            num = self.__size
            for m in range(num):
                if self.__position[1] > 0:
                    print(" ", end="")
                for n in range(num):
                    print("#", end="")
                print()

    """
    This is a property getter method, retrieves the
    set cordinates of the obj. square.
    """
    @property
    def position(self):

        return self.__position

    """
    This is a property setter method, sets the coordinates of the obj.
    square.
    """
    @position.setter
    def position(self, value):

        if type(value) != tuple:
            raise TypeError("position must be a tuple \
                            of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple \
                            of 2 positive integers")
        elif type(value[0]) and type(value[1]) != int:
            raise TypeError("position must be a tuple \
                            of 2 positive integers")
        else:
            self.__position = value
