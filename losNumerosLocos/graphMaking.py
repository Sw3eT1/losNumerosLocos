import numpy as np
import matplotlib.pyplot as plt

def makeGraph(f,a,b, zeroPointBi,zeroPointNe, wzor):
    xValues = np.linspace(a,b, 400)
    yValues = f(xValues)
    zeroY1 = f(zeroPointNe)
    zeroY2 = f(zeroPointBi)
    plt.plot(xValues, yValues, color='b')

    plt.scatter(zeroPointNe, zeroY1, color='red', s=50, label="Miejsce zerowe Newton")
    plt.scatter(zeroPointBi, zeroY2, color='green', s=50, label="Miejsce zerowe Bisekcja")

    plt.axhline(0, color='black', linewidth=0.8)  # Oś X
    plt.axvline(0, color='black', linewidth=0.8)  # Oś Y

    plt.xlim(a-0.5, b+0.5)

    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title(f'Wykres funkcji {wzor} z zaznaczonymi miejscami zerowymi')
    plt.legend()
    plt.grid()

    plt.show()