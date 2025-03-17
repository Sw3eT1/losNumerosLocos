
def newtonMethodEpsilon(f, x0, dfx, epsilon=1e-6):
    x = x0
    while True:
        if dfx == 0 or dfx(x) < 0.00000001:
            print("Error: Derivative is zero!")
            return None
        x_new = x - f(x) / dfx(x)
        if abs(x_new - x) < epsilon:
            return x_new
        x = x_new

def newtonMethodIterations(f, x0,dfx, numOfIter=10):
    x = x0
    for _ in range(numOfIter):
        if dfx == 0 or dfx(x) < 0.01:
            print("Error: Derivative is zero!")
            return None
        x = x - f(x) / dfx(x)
    return x