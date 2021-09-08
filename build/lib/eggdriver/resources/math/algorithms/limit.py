from eggdriver.resources.math.constants import inf
from eggdriver.resources.math.theoric import positiveInfinity, negativeInfinity, undefined

def lim(f, value):
    zero = 1 / inf
    below = f(value - zero)
    above = f(value + zero)
    if -zero <= below - above <= zero:
        result = (below + above) / 2
    else:
        return undefined.value
    if result >= inf:
        return positiveInfinity.value
    elif result <= -inf:
        return negativeInfinity.value
    elif -zero <= result <= zero:
        return 0
    return result
