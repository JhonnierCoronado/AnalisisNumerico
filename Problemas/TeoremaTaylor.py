import math

def taylor():
    a = 0
    r = f(a)
    for i in range (0, 100):
        r += (f(a) / math.factorial(i))*((0.05-a)**i)

    print ('%.5g' % r);    


def f(a):
    return math.exp(a)

taylor()