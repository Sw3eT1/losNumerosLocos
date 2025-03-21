def bisectionMethodEpsilon(f, a, b, epsilon=1e-6):
    if f(a) * f(b) > 0:
        print("Error: The function does not change sign in the given range!")
        return None
    howManyIterations = 0
    while (b - a) / 2 > epsilon:
        howManyIterations += 1
        c = (a + b) / 2
        if f(c) == 0 or (b - a) / 2 < epsilon:
            return c, howManyIterations

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2, howManyIterations


def bisectionMethodIterations(f, a, b, numOfIter=100):
    if f(a) * f(b) > 0:
        print("Error: The function does not change sign in the given range!")
        return None

    for val in range(numOfIter):
        c = (a + b) / 2
        if f(c) == 0:
            return c

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2
