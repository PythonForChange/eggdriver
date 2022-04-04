class LinearError(Exception):
    def __init__(self, type = 0):
        message = {
            0: "Vectors have to be of the same size",
            1: "Matrix must be a squared matrix",
            2: "The number of rows and columns must be a positive interger"
        }
        super().__init__(message[type])

def dot(a, b, autoExpand = False):
    result = 0
    if len(a) != len(b):
        if autoExpand:
            dualExpand(a, b)
        else:
            raise LinearError
    if len(a) != 0 and len(a) == len(b):
        for i in range(0, a.size):
            result += a[i] * b[i]
    return result

def dualExpand(a, b):
    if a.size < b.size:
        a.expand(b.size - a.size)
    else:
        b.expand(a.size - b.size)