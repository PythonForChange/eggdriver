from eggdriver.resources.math.polynomial import Polynomial
from eggdriver.resources.math.constants import series_inf
from math import factorial

def PowerSerie(n_term, number_of_terms = series_inf):
    sum = Polynomial(0)
    for n in range(number_of_terms):
        coef, exp = n_term(n)
        term = Polynomial(f"{coef}x^{exp}")
        sum = sum.plus(term)
    return sum

def cos_term(n):
    return ((-1) ** n) / factorial(2 * n), 2 * n

cos_serie = PowerSerie(cos_term)

def sin_term(n):
    return ((-1) ** n) / factorial(2 * n + 1), 2 * n + 1
    
sin_serie = PowerSerie(sin_term)

