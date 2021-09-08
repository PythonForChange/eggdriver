import math

def truncate(x, n):
    integer = int(x * (10**n))/(10**n)
    return float(integer)

def floor(x):
    return math.floor(x)

def ceil(x):
    return math.ceil(x)