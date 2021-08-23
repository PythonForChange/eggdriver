from eggdriver.resources.console.display import *
from eggdriver.resources.console.progress import *

def get(tag: str):
	i=input(blue+"$"+tag+"> "+green)
	return i

def put(content, colour = white):
	print(colour + content, end = "")