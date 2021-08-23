# Imports
from eggdriver.resources.strings import normalize

"""
FUNCTION varName(variable)

Returns the name of a variable from globals()

Eg:
variable = 3
print(varName(variable))
>>> variable

That includes the names of classes instances

Eg:
instance = MyClass()
print(varName(instance))
>>> instance
"""
def varName(variable):
    for name in globals():
        if eval(name) == variable:
            return(name)


"""
FUNCTION printVarName(variable)

Prints the name of a variable from globals()

Eg:
instance = MyClass()
printVarName(instance)
>>> instance
"""
def printVarName(variable):
    print(varName(variable))

"""
FUNCTION printVarName(variable)

Prints the type of a variable

Eg:
s = Stack(["pizza","pineapple"])
printVarType(s)
>>> egg.resources.structures.lists.Stack
"""
def printVarType(variable):
    t = str(type(variable))
    print(t[8:-2])

"""
CLASS var()

Ex:
number = var(3)
number.int
>>> 3
number.float
>>> 3.0
number.str
>>> 3
number.bool
>>> True

Ex:
word = var("true")
word.int
>>> 4
word.float
>>> 4.0
word.str
>>> true
word.bool
>>> True

Ex:
spanish_phrase = var("El camión es mío")
spanish_phrase.norm
>>> El camion es mio
"""
class var():
    def __init__(self, var):
        self.var = var
    @property
    def float(self):
        return float(self.int)
    @property
    def int(self):
        if isinstance(self.var, str):
            return len(self.var)
        return int(self.var) 
    @property
    def str(self):
        s=str(self.var)
        assert isinstance(s, str)
        return s
    @property
    def bool(self):
        if isinstance(self.var, str):
            if self.var.lower() == "true":
                return True
            else:
                return False 
        return bool(self.var) # If self.var==0, returns 0. Else, returns 1
    @property
    def norm(self): # Remove accents from words
        return normalize(self.str)

if __name__ == "__main__":
    If = "you are reading this,"
    you = var("are not importing this file")
    print(varName(If), If, varName(you), you.str) #Example of usage
