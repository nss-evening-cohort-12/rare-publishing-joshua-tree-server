class Category():
	def __init__(self, id, category_name):
		self.id = id
		self.category_name = category_name

	def __repr__(self):
		return f"{self.category_name} is a category."
