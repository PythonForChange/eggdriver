from eggdriver.resources.structures.lists import List

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
            raise Exception("Vectors have to be of the same size")
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
            raise Exception("Vectors have to be of the same size")
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

