from eggdriver import lim, inf, add, constant, positiveInfinity

def f(x):
    return 7

print(lim(f, inf))

print(add(constant(3), constant(5)))
print(add(constant(3), constant(positiveInfinity)))