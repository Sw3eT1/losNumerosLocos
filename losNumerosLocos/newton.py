def newtonMethodEpsilon(f, x0, dfx, epsilon=1e-6):
    x = x0
    howManyIterations = 0
    while True:
        howManyIterations += 1
        if dfx(x) == 0 or abs(dfx(x)) < 1e-8:
            print("Error: Derivative is zero!")
            return None
        x_new = x - f(x) / dfx(x)
        if abs(x_new - x) < epsilon:
            return x_new, howManyIterations
        x = x_new

def newtonMethodIterations(f, x0,dfx, numOfIter=10):
    x = x0
    for _ in range(numOfIter):
        if dfx(x) == 0 or abs(dfx(x)) < 1e-8:
            print("Error: Derivative is zero!")
            return None
        x = x - f(x) / dfx(x)
    return x