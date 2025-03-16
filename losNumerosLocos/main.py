# Funkcja wielomianowa: f(x)=x^3−4x
# Funkcja trygonometryczna: sin(x)-1/2
# Funkcja wykladnicza: 2^x-4
# Zlozenie tryg. i wielo. sin(x^2)-1/2

from time import sleep

mainDecision = False

while mainDecision == False:

    print("Chose a proper function:"
          "\n a) f(x)=x^3−4x"
          "\n b) f(x)=sin(x)-1/2"
          "\n c) f(x)=2^x-4"
          "\n d) f(x)=sin(x^2)-1/2")

    val = input("Select your option: ").lower()

    properOptions = ["a", "b", "c", "d"]

    if val not in properOptions:
        print("Invalid input!")
        sleep(1)
    else:
        mainDecision = True


properOptions = ["a", "b"]
subDecision = False

while subDecision == False:
    print("Chose if you want to: "
          "\n a) achive the pecified accuracy of calculation"
          "\n b) chose your numer of iterations")
    val = input("Select your option: ").lower()
    if val not in properOptions:
        print("Invalid input!")
        sleep(1)
    else:
        subDecision = True

match val:
    case "a":
        epsilon = input("Enter the value of ε for (|xi−xi−1|<ε)")
    case "b":
        numberOfIterations = input("Enter the number of iterations: ")