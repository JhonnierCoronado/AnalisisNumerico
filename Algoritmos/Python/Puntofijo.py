import math


def g(x):
    return math.e**x / math.pi
def invg(x):
    return math.log(x*math.pi)



def puntoFijo(a, b, x, error):
    cont = 1
    xi = x
    gxi = g(xi)
    up = False
    while math.fabs(xi * gxi) > error:
        if xi < a:
            up = True
        if up == False:
            xi = gxi
            gxi = g(xi)
        else:
            gxi = xi
            xi = invg(gxi)
        cont += 1
    return (xi, it)

def main():
    a = 0
    b = 0

    x = (a+b)/2.0
    (r, it) = puntoFijo(a, b, x, 10e-8)
    print ("El resultado es", r, "con", it, "iteraciones")


main()
