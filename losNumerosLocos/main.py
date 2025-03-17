# Funkcja wielomianowa: f(x)=x^3−4x
# Funkcja trygonometryczna: sin(x)-1/2
# Funkcja wykladnicza: 2^x-4
# Zlozenie tryg. i wielo. sin(x^2)-1/2

import numpy as np
from math import sin
from time import sleep

from bisection import bisectionMethodEpsilon, bisectionMethodIterations
from graphMaking import makeGraph
from losNumerosLocos.horner import horner

mainDecision = False

while not mainDecision:

    print("Chose a proper function:"
          "\n a) f(x)=x^2−4x"
          "\n b) f(x)=sin(x)-1/2"
          "\n c) f(x)=2^x-4"
          "\n d) f(x)=sin(x^2)-1/2")

    val = input("Select your option: ").lower()

    properOptions = ["a", "b", "c", "d"]

    if val not in properOptions:
        if val == "":
            print("You have entered an empty string!")
        else:
            print("Invalid input!")
            sleep(1)
    else:
        mainDecision = True

match val:
    case "a":
        coefficients = [1, 0, -4]  #x^2 + 0*x - 4
        f = lambda x: horner(x, coefficients)
    case "b":
        f = lambda x: np.sin(x) - 1/2
    case "c":
        f = lambda x: 2**x - 4
    case "d":
        f = lambda x: np.sin(np.pow(x,2)) - 1/2

properOptions = ["a", "b"]

intervalDecision = False

while not intervalDecision:
    try:
        lowerInterval = float(input("Select lower value for the interval: "))
        higherInterval = float(input("Select higher value for the interval: "))

        if higherInterval <= lowerInterval:
            print("Invalid input! Please choose a second value as the greater one.")
            sleep(1)
        else:
            intervalDecision = True

    except ValueError:
        print("Invalid input! Please enter numerical values only.")
        sleep(1)

subDecision = False

while subDecision == False:
    print("Chose if you want to: "
          "\n a) achieve the specified accuracy of calculation"
          "\n b) chose your numer of iterations")
    val = input("Select your option: ").lower()
    if val not in properOptions:
        print("Invalid input!")
        sleep(1)
    else:
        subDecision = True

if val == "a":
    while True:
        try:
            epsilon = float(input("Enter the value of ε for (|xi−xi−1|<ε): "))
            break
        except ValueError:
            print("Invalid input! Please enter numerical values only.")
            sleep(1)
    resultEpsilon = bisectionMethodEpsilon(f, lowerInterval,higherInterval,epsilon)
    if resultEpsilon is not None:
        print(f'Estimated value of a zero place of a given function is: {resultEpsilon}')
        makeGraph(f, lowerInterval, higherInterval, resultEpsilon)
    else:
        print("No valid zero point found, skipping graph drawing.")
elif val == "b":
    while True:
        try:
            numberOfIterations = int(input("Enter the number of iterations: "))
            if numberOfIterations > 0:
                break
            else:
                print("Invalid input! Please enter a positive integer.")
        except ValueError:
            print("Invalid input! Please enter an integer value.")
        sleep(1)
    resultIterations = bisectionMethodIterations(f, lowerInterval, higherInterval, numberOfIterations)
    if resultIterations is not None:
        print(f'Estimated value of a zero place of a given function is: {resultIterations}')
        makeGraph(f, lowerInterval, higherInterval, resultIterations)
    else:
        print("No valid zero point found, skipping graph drawing.")