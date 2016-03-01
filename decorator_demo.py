Class Balloon(object):
""" This class show the use static data, static method and decorator"""
	
	unique_colors = set()

	def __init__(self,color):
		self.color = color
		Balloon.unique_colors.add(color)
	
	@staticmethod
	def unique_color_count():
		return len(Balloon.unique_colors)

	@staticmethod
	def unique_colors():
		return Balloon.unique_colors.copy()
