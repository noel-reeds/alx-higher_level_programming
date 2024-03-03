#!/usr/bin/python3
"""A square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
	"""class square"""
	def __init__(self, size, x=0, y=0, id=None):
		"""Init method"""
		super().__init__(size, size, x, y, id)
		self.size = size
		self.__width = self.__height = self.size

	def __str__(self):
		"""custom str method"""
		return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
