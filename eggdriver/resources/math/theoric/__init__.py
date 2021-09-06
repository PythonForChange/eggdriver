class infinity():
    def __init__(self, name):
        self.value = name

class constant():
    def __init__(self, x):
        self.value = x

def isConstant(x):
    return type(x) == constant

positiveInfinity = infinity("positiveInfinity")
negativeInfinity = infinity("negativeInfinity")
undefined = infinity("undefined")

def isInfinity(x):
    return (x in [positiveInfinity, negativeInfinity, undefined])

def add(x, y):
    if isConstant(x) and isConstant(y):
        return x.value + y.value
    elif isConstant(x) and isInfinity(y):
        return y.value
    elif isConstant(y) and isInfinity(x):
        return x.value
    elif isInfinity(x) and isInfinity(y):
        if x == y:
            return x.value
        else:
            return undefined.value

def multiply(x, y):
    if x == undefined or y == undefined:
        return undefined
    elif isConstant(x) and isConstant(y):
        return x.value * y.value
    if isConstant(x) and isInfinity(y):
        if x == 0:
            return undefined.value
        elif x > 0:
            return y.value
        elif y == positiveInfinity:
            return negativeInfinity.value
        else:
            return positiveInfinity.value
    if isConstant(y) and isInfinity(x):
        return multiply(y, x)
    if isInfinity(x) and isInfinity(y):
        if x == y:
            return positiveInfinity.value
        else:
            return negativeInfinity.value

class variable():
    pass