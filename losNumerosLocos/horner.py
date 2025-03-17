def horner(x, coeffs):
    result = coeffs[0]
    for coeff in coeffs[1:]:
        result = result * x + coeff
    return result
