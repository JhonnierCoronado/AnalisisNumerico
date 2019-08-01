import math

#Para funcion exp(x) - pi * x
def f(x):
    return math.exp(x) - math.pi * x

def aitken(x1, error):
    n = 1
    x2 = 0.0
    fx = f(x1)
    while (math.fabs(x1 - fx) >= error):
        x1 = fx
        fx = f(x1)
        n += 1
        x2 = fx
        fx = f(x2)
        n += 1
        x1 = fx - ((fx - x2) ** 2 ) / (fx - 2 * x2 + x1)
        fx = f(x1)
        n += 1
    return (n, fx)

x1 = 1
error = 10e-8
(it, raiz) =  aitken(x1, error)

print("Con ", it, " iteraciones, se tiene una raiz de (con 5 cifras)",'%.4f'%raiz)