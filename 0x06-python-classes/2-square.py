#!/usr/bin/python3
"""
This is a class representing a square
"""


class Square:
    """
    This is an empty class, defines a square
    A square is a four-sided shape with equal sides.
    """
    def __init__(self, size=0):
        """
        The __init__ method is the constructor for the class
        Logic for the method will be added later.

        Args:
            size(int): The size of the obj. square.
        """
        self.__size = size
        if type(size) != int:
            print("size must be an integer")
        elif size < 0:
            print("size must be >= 0")
