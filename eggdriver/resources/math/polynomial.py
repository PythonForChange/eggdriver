from eggdriver.resources.math.linear import Vector, dualExpand, vectorize
from eggdriver.resources.math.algorithms.solver import solve
from eggdriver.resources.structures.objects import varName

def x(var):
    return var

class Polynomial(Vector):
    def __init__(self, poly = [], variable = x):
        if type(poly) != list:
            if type(poly) != str:
                poly = [poly]
            else:
                poly = vectorize(poly)
        super().__init__(poly)
        self.variable = variable
    def display(self):
        result = Polynomial()
        nonZeros = 0
        if self.size != 0:
            for i in range(0, self.size):
                if self[i] > 0:
                    nonZeros += 1
                if self[i] > 0 and nonZeros > 1:
                    result.append("+" + str(self[i]) + x_powered(i, self.var))
                elif self[i] != 0:
                    result.append(str(self[i]) + x_powered(i, self.var))
        text = ""
        for i in result:
            text += i + " "
        print(text)
    def plus(self, vector):
        return plusPoly(self, vector)
    def times(self, vector):
        return times(self, vector)
    def power(self, exponent):
        result = Polynomial(1)
        for i in range(0, exponent):
            result = result.times(self)
        return result
    def eval(self, x):
        result = 0
        for i in range(0, self.size):
            f = self[i]
            result += f * (self.variable(x) ** i)
        return result
    @property
    def var(self):
        name = varName(self.variable)
        if name != None:
            return name
        return "x"
         
    @property
    def zeros(self):
        return solve(self.eval, degree = self.degree)
    @property
    def degree(self):
        deg = 0
        for i in range(0, self.size):
            if self[i] != 0:
                deg = i
        return deg

def x_powered(i, variable = "x"):
    if i == 0 :
        return ""
    elif i == 1:
        return variable
    return f"{variable}^{i}"

def plusPoly(a, b):
    if type(a) != Polynomial:
        a = Polynomial([a])
    if type(b) != Polynomial:
        b = Polynomial([b])
    result = Polynomial()
    if len(a) != len(b):
        dualExpand(a, b)
    if len(a) != 0 and len(a) == len(b):
        for i in range(0, a.size):
            result.append(a[i] + b[i])
    return result

def scalePoly(polynomial, scalar):
    result = Vector()
    if polynomial.size != 0:
        for i in polynomial:
            result.append(scalar * i)
    return result

def times(a, b):
    result = Polynomial()
    if len(a) != 0:
        for i in range(0, len(a)):
            product = Polynomial()
            for j in range(0, i):
                product.append(0)
            for j in b.scale(a[i]):
                product.append(j)
            result = result.plus(product)
    return result

def fromZeros(zeros = []):
    result = Polynomial(1)
    for i in zeros:
        result = Polynomial([-i, 1]).times(result)
    return result


