# MC intergral
import numpy as np
import matplotlib.pyplot as plt
from random import random
import scipy as sci
from numba import jit

@jit
def f1(x):
    return sci.sqrt(1-(x-1)**2)
@jit
def f2(x):
    return (2 - sci.sqrt(4 - x**2))


@jit
def MC(N):
    count = 0
    for i in range(N):
        x = 2 * random()
        y = random()
        if y < f1(x) and y > f2(x) and x > 0 and x < 0.6:
            count += 1
    I = 2*count/N
    return I


#MC(1000)


@jit
def error(num, tests):
    error_array = []
    for i in range(tests):
        error_array.append(MC(num))
    std = np.std(error_array)
    return std


@jit
def plotter(limit=100000):
    deviance_array = []
    y = 10
    x = []
    while y <= limit:
        deviance_array.append(error(y, 100))
        x.append(y)
        y = y * 10
    print("The area between the curves is:")
    print(MC(limit))
    
    plt.plot(deviance_array)
    plt.xticks([])
    plt.title("Standard Deviation")
    plt.xlabel("Amount of points placed")
    plt.ylabel("Seconds")
    plt.show()

plotter(1000)