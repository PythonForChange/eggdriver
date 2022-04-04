from eggdriver.resources.structures.lists import Set
from eggdriver.resources.math.algorithms.solver.dichotomy import root
from eggdriver.resources.math.constants import R, inf

def solve(function, bias = 0, domain = R,  accurancy = 16, degree = 1, alerts = True):
    roots = Set()
    count = 0
    customDomain = domain != R
    while roots.size < degree and count < inf:
        if not customDomain:
            domain = [- 2.0 ** int(count), 2.0 ** int(count)]
        r = root(function, -bias, domain, accurancy)
        roots.insert(str(r))
        if alerts:
            print(degree - roots.size, "solutions remaining")
        count += 1 / (2 * degree)
    return roots