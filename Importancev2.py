import scipy as sci
from scipy.integrate import quad
import random as rand

def f(x):
    return (((x ** (-1))/(sci.exp(x) + 1)))

def w(x):
    return x ** (-1)

def first_sum(N):
    the_sum = 0
    for i in range(N):
        x= rand.random()
        the_sum = the_sum + f(x)/w(x)

    return the_sum

def second_integral(a,b):
    return quad(w, a, b)[0]

def answer(N, a, b):
    return 1/N * first_sum(N)*second_integral(a,b)

print(answer(1000,0,1))