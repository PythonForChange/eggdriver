import eggdriver.nqs.core as core
from eggdriver.resources.extensions import py

def write(name: str):
	T=core.compile(name)
	py.write(T,name)