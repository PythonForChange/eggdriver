def derive(poly, n: int = 1):
    p = poly
    if n >= 1:
        for deg in range(n):
            der_poly = p
            for i in range(p.size):
                der_poly[i] = 0
                if i < p.size - 1:
                    der_poly[i] = p[i + 1] * (i + 1)
            p = der_poly
    return p


    

