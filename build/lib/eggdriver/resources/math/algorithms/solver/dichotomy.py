import random
from eggdriver.resources.math.constants import R
from eggdriver.resources.math.float import truncate

def root(function, bias = 0, domain = R,  accurancy = 16):
    """Gives a root of function(x) = bias, in a certain domain"""
    error = 10 ** (- accurancy - 100)
    while True:
        bound = [random.uniform(domain[0], domain[1]), random.uniform(domain[0], domain[1])]
        bound.sort()
        a, b = bound[0], bound[1]
        fa = function(a) - bias
        fb = function(b) - bias
        if fa * fb < 0:
            break
    for i in range(100):
        mean = (a + b) / 2
        fm = function(mean) - bias
        if abs(fm) < error:
            return round(mean, accurancy)
        if fa * fm < 0:
            b = mean
        else:
            a = mean
    return "There is not a root in this domain"