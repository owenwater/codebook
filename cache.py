class Cache(object):
	def __init__(self):
		self.clear()

	def write(self, s):
		self.s += s

	def get(self):
		return self.s
	
	def clear(self):
		self.s = ""


