Class Rectangle(object):
""" This class represents a rectangle"""

	def __init__(self,width,height):
		self.width = width
		self.height = height
	def _width(self):
		return self.__width

	def _set_width(self,width):
		self.__width = width
	
	def _area(self):
		return self.width * self.height

	width = property(fget = _width,fset = _set_width)

# How to use class
rect = Rectangle(50,20)
print rect.area()
rect.width = 100
