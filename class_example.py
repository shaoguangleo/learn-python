Class Rectangle(object):
""" This class represents a rectangle"""

	def __init__(self,width,height):
		self.width = width
		self.height = height
	
	def get_width(self):
		return self.width

	def set_width(self,width):
		self.width = width
	
	def get_height(self):
		return self.height

	def area(self):
		return self.get_width() * self.get_height()

# How to use class
rect = Rectangle(50,20)
print rect.area()
rect.set_width(100)
print rect.get_width()
