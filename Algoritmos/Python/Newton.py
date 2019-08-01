import math


def f(x):
    return (x - 1.35) ** 3

def derivada(x):
    return 3 * (x - 1.35) ** 2


def newton(x, error):
    cont = 0
    result = x
    fx = f(x)

    while math.fabs(fx) > error:
        result = result - f(result) / derivada(result)
        fx = f(result)
        cont += 1
    return (result, cont)

x = 1
(r, it) = newton(x, 1e-8)
print("Con un error de: ", 1e-8)
print("da una raiz de: ", r, " con ", it, " iteraciones")