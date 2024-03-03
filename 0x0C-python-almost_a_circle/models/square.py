#!/usr/bin/python3
"""A square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Init method"""
        super().__init__(size, size, x, y, id)
        self.__width = self.__height = size

    def __str__(self):
        """custom str method"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """retrieves the size attrs"""
        return self.__width

    @size.setter
    def size(self, value):
        """sets the size attrs"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """updates a square"""
        attrs = ["id", "size", "x", "y"]
        if args:
            for index, value in enumerate(args):
                setattr(self, attrs[index], args[index])
        for key in kwargs.keys():
            if key in attrs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """object to dictionary representation"""
        return {
                "id": self.id, "size": self.__width,
                "x": self.x, "y": self.y
              }
