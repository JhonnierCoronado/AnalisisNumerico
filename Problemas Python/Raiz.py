import math

def raiz(n, E, x):
    y = float(0)
    contador = 0
    while(math.fabs(x-y) > E):
        y = n/x + x
        y = y/2
        x = y
        contador += 1
    return (y, contador)


(result, it) = raiz(7.0, 0.01, 2)
print("Se obtiene el resultado de ", result, ". Con ", it, " iteracciones")