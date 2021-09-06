from eggdriver import lim, inf, add, constant, positiveInfinity, Polynomial

def f(x):
    return x**2

print(lim(f, inf))

def g(x):
    return 1 / x

print(lim(g, inf))

v = Polynomial([0, 2, 0, 9])
ww = v.power(3)
v.display()
ww.display()



print(add(constant(3), constant(5)))
print(add(constant(3), constant(positiveInfinity)))