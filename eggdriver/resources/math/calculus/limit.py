from eggdriver.resources.math.constants import inf
from eggdriver.resources.math.float import truncate
from eggdriver.resources.math.theoric import positiveInfinity, negativeInfinity, undefined
from eggdriver.resources.structures.objects import varName

def lim(f, value):
    zero = 1 / inf
    below = f(value - zero)
    above = f(value + zero)
    error = inf ** (-0.5)
    if -error <= below - above <= error:
        result = (below + above) / 2
        floating = str(result).split(".")
        if len(floating) == 2:
            decimals = len(floating[1])
            result = round(result, decimals - 1)
            result = truncate(result, decimals - 2)
    else:
        print(f"""Limit of {varName(f)} function at value is undefined
Reason: Lateral limits are not equal
Below: {below}
Above: {above}""")
        return undefined.valuei
    if result >= inf:
        return positiveInfinity.value
    elif result <= -inf:
        return negativeInfinity.value
    elif -zero <= result <= zero:
        return 0
    return result
