from eggdriver import lim, inf, add, constant, positiveInfinity, Polynomial, pi

def f(x):
    return x**2

print(lim(f, inf))

def g(x):
    return 1 / x

print(lim(g, inf))

u = Polynomial([0, -49, 0, 1]).times(Polynomial([-3.9, 1]))
v = u.times(Polynomial([-2, 1])).times(Polynomial([-11, 1]))
v.display()
print(v.zeros)


print(add(constant(3), constant(5)))
print(add(constant(3), constant(positiveInfinity)))