def bisectionMethodEpsilon(f, a, b, epsilon=1e-6):

    if f(a) * f(b) > 0:
        print("Error: The function does not change sign in the given range!")
        return None

    while (b - a) / 2 > epsilon:
        c = (a + b) / 2
        if f(c) == 0 or (b - a) / 2 < epsilon:
            return c

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2


def bisectionMethodIterations(f, a, b, numOfIter=100):

    if f(a) * f(b) > 0:
        print("Error: The function does not change sign in the given range!")
        return None

    for _ in range(numOfIter):
        c = (a + b) / 2
        if f(c) == 0:
            return c

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2
