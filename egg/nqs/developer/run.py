from egg.nqs.developer.write import write
from egg.resources.extensions import py

def run(name: str):
    write(name)
    py.execute(name)