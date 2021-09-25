from eggdriver.resources.math.constants import inf

def derive(poly):
    der_poly = poly
    for i in range(poly.size):
        der_poly[i] = 0
        if i < poly.size - 1:
            der_poly[i] = poly[i + 1] * (i + 1)
    return der_poly

def derivative(f):
    h = 1 / inf
    def d(x):
        (f(x + h) - f(x)) / h
    return d