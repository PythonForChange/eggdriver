from eggdriver.resources.console.display import *
from eggdriver.resources.console.progress import *
from eggdriver.resources.constants import white, blue, green

def get(tag: str):
	i = input(blue + "$" + tag + "> " + green)
	return i

def put(content, colour = white, ending = ""):
	print(colour + content, end = ending)

def pg(content: str, tag :str = "egg"):
	"""Print content and get an input"""
	print(white + content)
	g = get(tag)
	return g