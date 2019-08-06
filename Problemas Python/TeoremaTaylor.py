import math

def taylor(x):
    a = 0
    r = 0
    for i in range (0, 15):
        r += (x**i / math.factorial(i))

    print ('%.5g' % r);    


def f(a):
    return math.exp(a)

taylor(0.5)