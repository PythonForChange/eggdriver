from eggdriver.resources.math.algorithms.solver.dichotomy import root
from eggdriver.resources.math.constants import e

def pow(base: float = 10, x: float = 0):
    return base ** x

def log(base: float = 10, x: float = 10, domain = [0, 0]):
    if domain == [0, 0]:
        domain = [0, x]
    def f(value):
        return pow(base, value)
    return root(f, x, domain, 8)

def ln(x):
    return log(e, x, [0, x])