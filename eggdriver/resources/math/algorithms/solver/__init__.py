from eggdriver.resources.structures.lists import Set
from eggdriver.resources.math.algorithms.solver.dichotomy import root
from eggdriver.resources.math.constants import R

def solutions(function, bias = 0, domain = R,  accurancy = 16, grade = 1):
    roots = Set()
    while roots.size < grade:
        r = root(function, bias, domain, accurancy)
        roots.insert(r)
    return roots