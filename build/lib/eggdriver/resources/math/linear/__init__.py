from eggdriver.resources.structures.lists import List
from eggdriver.resources.utils import indexes
from eggdriver.resources.math.linear.utils import *

class Vector(List):
    def __init__(self, vanillaList = []):
        if type(vanillaList) == str:
            temp = vanillaList.replace("[", "").replace("]", "")
            vanillaList = list(map(int, temp.split()))
        super().__init__(vanillaList)
    def plus(self, vector):
        return plus(self, vector)
    def dot(self, vector):
        return dot(self, vector)
    def scale(self, scalar):
        return scale(self, scalar)
    def expand(self, scalar):
        [self.append(0) for i in range(0, scalar)]

class Matrix(Vector):
    def __init__(self, vectorOfVectors = [], rows = 1, columns = 1, auto_size = True):
        if vectorOfVectors == []:
            vectorOfVectors = Vector()
            for j in range(columns):
                v = Vector()
                v.expand(rows)
                vectorOfVectors.append(v)
        elif type(vectorOfVectors) == str:
            if rows == 0 or columns == 0:
                raise LinearError(2)
            else:
                temp1 = vectorOfVectors.replace("|", "")
                if auto_size:
                    temp2 = temp1.split("\n")
                    temp3 = temp2[1] # Index is 1 because temp2[0] always is a void string ""
                    columns = len(temp3.split()) 
                M = list(map(int, temp1.split()))       
                output = [M[i:i + columns] for i in range(0, len(M), columns)]
                vectorOfVectors = list(map(Vector, output))
        super().__init__(vectorOfVectors)
    def display(self):
        for i in self:
            print(i.display(True, ["|", "|"]))
    @property
    def det(self):
        return determinant(self)
    @property
    def n(self):
        return len(self)
    @property
    def m(self):
        return len(self[0])

def rowReduce(matrix: Matrix):
    result = Vector()
    return result

def determinant(M):
    result = M[0][0]
    if M.n != M.m:
        raise LinearError(1)
    elif M.n > 1:
        row = M[0]
        result = 0
        for i in indexes(row):
            minor = subMatrix(M, 0, i)
            result = result + (((-1) ** i) * M[0][i] * determinant(minor))
    return result

def subMatrix(M, row, column):
    result = Matrix()
    for i in range(M.n):
        if i != row:
            v = Vector()
            for j in range(M.m):
                if j != column:
                    v.append(M[i][j])
            result.append(v)
    return result

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