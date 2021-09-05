from eggdriver.resources.math.constants import inf

def lim(f, value):
    result = f(value - 0.00000000001)
    if result >= inf:
        return "inf"
    elif result <= -inf:
        return "-inf"
    return result
