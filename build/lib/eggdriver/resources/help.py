from eggdriver.resources.constants import white
from eggdriver.resources.extensions import py

def help():
    """Get help from Egg"""
    T = "Welcome to Egg:\nThe Egg-cosystem console\n\n"
    T += py.read("egg/library/commands")
    print(white + T)
    return "done"