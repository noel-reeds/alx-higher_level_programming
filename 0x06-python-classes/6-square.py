#!/usr/bin/python3
"""
This is a class representing a square
"""


class Square:
    """
    This is an empty class, defines a square
    A square is a four-sided shape with equal sides.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        The __init__ method is the constructor for the class
        Logic for the method will be added later.

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

    def area(self):
        """
        This is the area method of the class Square.
        Area is computed by size * size or size-squared
        """
        area = self.__size ** 2  #: Area computation..size-squared.
        return area

    @property
    def size(self):
        """
        Retrieves the size of the obj. square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets or modifies the the size of the obj. with a new value.
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """
        This is a public instance method.
        Prints a square of "#" to stdout..
        """
        if self.__size == 0:
            print()
        else:
            num = self.__size
            for m in range(num):
                for n in range(num):
                    if position[1] > 0:
                        print("_", end="")
                    else:
                        print("#", end="")
                print()
