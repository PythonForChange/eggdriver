from egg.resources.constants import white
from egg.resources.extensions import txt

def help():
    T="Welcome to Pyfoch Egg:\nThe Pyfoch Egg-cosystem console\n\n"
    T+=txt.read("egg/library/commands")
    print(white+T)
    return "done"