import egg.nqs.core as core
from egg.resources.extensions import py

def write(name: str):
	T=core.compile(name)
	py.write(T,name)