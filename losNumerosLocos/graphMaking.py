import numpy as np
import matplotlib.pyplot as plt

def makeGraph(f,a,b, zeroPoint):
    xValues = np.linspace(a,b, 400)
    yValues = f(xValues)
    zeroY = f(zeroPoint)
    plt.plot(xValues, yValues, color='b')

    plt.scatter(zeroPoint, zeroY, color='red', s=50, label="Miejsce zerowe")

    plt.axhline(0, color='black', linewidth=0.8)  # Oś X
    plt.axvline(0, color='black', linewidth=0.8)  # Oś Y

    plt.xlim(a, b)

    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Wykres funkcji f(x) z zaznaczonym miejscem zerowym")
    plt.legend()
    plt.grid()

    plt.show()