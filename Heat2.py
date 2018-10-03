from scipy import integrate
import numpy as np
import cmath as math
import matplotlib.pyplot as plt



def capacity(T=500, vol=1000, rho=2.7, Debye=428):

    f = lambda x: ((x**4*np.exp(x))/(np.exp(x)-1)**2)
    integral = integrate.quad(f,5,500)[0]
    k = 1.38e-23

  #  f keeps spit out wrong tiny numbers, but I cant see whats wrong?
    print(integral)
    Cv = 9 * vol * rho * k  * integral

    return Cv

def array_builder(T):
    array = []

    for i in range(T):
        array.append(capacity(i))

    return array


def plotter(T):

    y_array = array_builder(T)
    x = np.linspace(5,T,1)
    print(y_array[34])
    y = y_array[x]
    plt.plot(x, y)
    plt.show()
plotter(100)