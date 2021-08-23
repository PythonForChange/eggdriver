from eggdriver.resources.constants import white
from eggdriver.resources.extensions import py

def help():
    T = "Welcome to Pyfoch Egg:\nThe Pyfoch Egg-cosystem console\n\n"
    T += py.read("egg/library/commands")
    print(white + T)
    return "done"