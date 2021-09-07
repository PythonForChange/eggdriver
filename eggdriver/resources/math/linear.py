from eggdriver.resources.structures.lists import List
from eggdriver.resources.utils import indexes

def dualExpand(a, b):
    if a.size < b.size:
        a.expand(b.size - a.size)
    else:
        b.expand(a.size - b.size)

def plus(a, b, autoExpand = False):
    result = Vector()
    if len(a) != len(b):
        if autoExpand:
            dualExpand(a, b)
        else:
            raise LinearError
    if len(a) != 0 and len(a) == len(b):
        for i in range(0, a.size):
            result.append(a[i] + b[i])
    return result

def dot(a, b, autoExpand = False):
    result = 0
    if len(a) != len(b):
        if autoExpand:
            dualExpand(a, b)
        else:
            raise LinearError
    if len(a) != 0 and len(a) == len(b):
        for i in range(0, a.size):
            result += a[i] * b[i]
    return result

def scale(vector, scalar):
    result = Vector()
    if vector.size != 0:
        for i in vector:
            result.append(scalar * i)
    return result

def vectorize(poly: str):
    """Transform a string polynomial into a coordinates vector"""
    p = poly.split(" ")
    result = Vector()
    coefs = List()
    exps = List()
    for i in p:
        temp = i + "^1"
        monomial = temp.strip("+").split("^")
        c = monomial[0].strip("x")
        if c == "":
            coef = 1.0
        else:
            coef = float(c)
        exp = int(monomial[1])
        if "x" not in i:
            exp = 0
        coefs.append(coef)
        exps.append(exp)
    degree = 0
    for i in indexes(exps):
        if exps[i] > degree:
            degree = exps[i]
    result.expand(degree + 1)
    for i in indexes(coefs):
        result[exps[i]] += coefs[i]
    return result

class Vector(List):
    def __init__(self, list = []):
        super().__init__(list)
    def plus(self, vector):
        return plus(self, vector)
    def dot(self, vector):
        return dot(self, vector)
    def scale(self, scalar):
        return scale(self, scalar)
    def expand(self, scalar):
        [self.append(0) for i in range(0, scalar)]

class Matrix(Vector):
    def __init__(self, n, m):
        vectorOfVectors = Vector()
        for i in range(m):
            v = Vector()
            v.expand(n)
            vectorOfVectors.append(v)
        super().__init__(vectorOfVectors)
    def display(self):
        for i in self:
            print(i.display(True, ["(", ")"]))

class LinearError(Exception):
    def __init__(self, type = 0):
        message = {
            0: "Vectors have to be of the same size"
        }
        super().__init__(message[type])
