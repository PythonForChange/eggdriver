from eggdriver.resources.math.algorithms.solver.dichotomy import root
from eggdriver.resources.math.calculus.limit import lim
from eggdriver.resources.math.constants import e
from eggdriver.resources.math.calculus.series import cos_serie, sin_serie

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

def cos(x):
    return cos_serie.eval(x)

def sin(x):
    return sin_serie.eval(x)

def tan(x):
    def tan_function(x):
        return sin(x) / cos(x)
    return lim(tan_function, x)