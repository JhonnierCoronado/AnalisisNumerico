# Metodo de la secante para f(x) = exp(x) - (2*x^3)


import math


def f(x):
    return math.exp(x) * (2 * (x**3))


def secante(x1, x2, error):
    x3 = 0.0
    fx1 = 0.0
    fx2 = 0.0
    fx3 = 0.0

    if math.fabs(f(x1)) < math.fabs(f(x2)):
        aux = x1
        x1 = x2
        x2 = aux
    
    fx1 = f(x1)
    fx2 = f(x2)

    while True:
        x3 = x2 - (fx2 * (x1 - x2)) / (fx1 - fx2)
        fx3 = f(x3)
        x1 = x2
        x2 = x3
        fx1 = f(x1)
        fx2 = f(x2)
        fx3 = f(x3)
        if math.fabs(fx3) > error:
            break
    
    return x3

x1 = 0
x2 = 3
secante(x1, x2, 10e-9)