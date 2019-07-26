import math

def raiz(n, E, x):
    y = float(0)
    while(math.fabs(x-y) > E):
        y = n/x + x
        y = y/2
        x = y
    return y

print(raiz(7.0, 0.1, 2))