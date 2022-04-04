class Parser():
	"""Pfcf files parser"""
	def __init__(self, name: str = "Parser"):
		self.sep = [',']
		self.sec = ['|']
		self.ski = ["\""]
		self.vip = ["\\"]
		self.den = ["~"]
		self.name = name
	def compare(self, x: str, arr):
		k = False
		for i in arr:
				k =( k or x == i)
		return k
	def separator(self, x: str ):
		return self.compare(x, self.sep)
	def section(self, x: str):
		return self.compare(x, self.sec)
	def skip(self, x: str):
		return self.compare(x, self.ski)
	def isVip(self, x: str):
		return self.compare(x, self.vip)
	def isDeny(self, x: str):
		return self.compare(x, self.den)