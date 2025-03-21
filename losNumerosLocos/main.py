# Funkcja wielomianowa: f(x)=x^3-4x-4
# Funkcja trygonometryczna: sin(x)-1/2
# Funkcja wykladnicza: 2^x-4
# Zlozenie tryg. i wielo. sin(x^2)-1/2

import numpy as np
from time import sleep

from bisection import bisectionMethodEpsilon, bisectionMethodIterations
from graphMaking import makeGraph
from horner import horner
from newton import newtonMethodEpsilon, newtonMethodIterations

mainDecision = False

wzory = ["f(x)=x^3-4x-4", "f(x)=sin(x)-1/2", "f(x)=2^x-4", "f(x)=sin(x^2)-1/2"]

while not mainDecision:

    print("Chose a proper function:"
          "\n a) f(x)=x^3-4x-4"
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
        coefficients = [1, 0,-4, -4]  #x^3-4x-4
        f = lambda x: horner(x, coefficients)
        dfx = lambda x: 3*x**2-4
        wzor = wzory[0]
    case "b":
        f = lambda x: np.sin(x) - 1/2
        dfx = lambda x: np.cos(x)
        wzor = wzory[1]
    case "c":
        f = lambda x: 2**x - 4
        dfx = lambda x: np.log(2) * 2**x
        wzor = wzory[2]
    case "d":
        f = lambda x: np.sin(np.pow(x,2)) - 1/2
        dfx = lambda x: 2*x * np.cos(x**2)
        wzor = wzory[3]

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

x0 = None
while x0 is None:
    try:
        x0 = float(input("Enter the starting point for Newton's method: "))
    except ValueError:
        print("Invalid input! Please enter a numerical value.")

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
    method = "epsilon"
    while True:
        try:
            epsilon = float(input("Enter the value of ε for (|xi−xi−1|<ε): "))
            break
        except ValueError:
            print("Invalid input! Please enter numerical values only.")
            sleep(1)
    resultBisectionEpsilon, howManyIterationsBisection = bisectionMethodEpsilon(f, lowerInterval, higherInterval, epsilon)
    resultNewtonEpsilon, howManyIterationsNewton = newtonMethodEpsilon(f,x0,dfx,epsilon)
    if resultBisectionEpsilon is not None:
        print(f'Estimated value of a bisection calculated zero place of a given function is: {resultBisectionEpsilon}\n')
        print(f'Number of iterations for bisection method with epsilon : {howManyIterationsBisection}\n')
        print(f'How bisection is close to zero: {f(resultBisectionEpsilon)}\n')
        print(f'Estimated value of a Newton calculated zero place of a given function is: {resultNewtonEpsilon}')
        print(f'Number of iterations for Newton method with epsilon : {howManyIterationsNewton}\n')
        print(f'How newton is close to zero: {f(resultNewtonEpsilon)}\n')
        makeGraph(f, lowerInterval, higherInterval, resultBisectionEpsilon,resultNewtonEpsilon, wzor,method)
    else:
        print("No valid zero point found, skipping graph drawing.")
elif val == "b":
    method = "iteracji zadanychb"
    while True:
        try:
            numberOfIterations = int(input("Enter the number of iterations: "))
            if 0 < numberOfIterations < 10000:
                break
            else:
                print("Invalid input! Please enter a positive integer.")
        except ValueError:
            print("Invalid input! Please enter an integer value.")
        sleep(1)
    resultBisectionIterations = bisectionMethodIterations(f, lowerInterval, higherInterval, numberOfIterations)
    resultNewtonIterations = newtonMethodIterations(f, x0,dfx, numberOfIterations)
    if resultBisectionIterations is not None:
        print(f'Estimated value of a bisection calculated zero place of a given function is: {resultBisectionIterations}\n')
        print(f'How bisection is close to zero: {f(resultBisectionIterations)}\n')
        print(f'Estimated value of a Newton calculated zero place of a given function is: {resultNewtonIterations}')
        print(f'How newton is close to zero: {f(resultNewtonIterations)}\n')
        makeGraph(f, lowerInterval, higherInterval,resultBisectionIterations,resultNewtonIterations,wzor,method)
    else:
        print("No valid zero point found, skipping graph drawing.")