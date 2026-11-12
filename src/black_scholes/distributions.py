import math


def normal_pdf(x):

    a= -1*(x**2)/2
    b= 1/(math.sqrt(2*math.pi))
    return b*math.exp(a)

def normal_cdf(x):
    x=x/math.sqrt(2)
    a= 1 + math.erf(x)
    return a/2

