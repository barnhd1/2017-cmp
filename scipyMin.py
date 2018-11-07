import numpy as np
from scipy.optimize import minimize

def f2(x):
    return 1/2 * x[0] ** 2 + 1/3 * x[1] ** 2 - x[0] * x[1] / 4

def init(x_min, x_max, y_min, y_max):
    x0 = x_min+np.random.random()*(x_max-x_min)
    y0 = y_min+np.random.random()*(y_max-y_min)
    return [x0, y0]
x_min, x_max = -4, 4
y_min, y_max = -4, 4  

[x0, y0] = init(x_min, x_max, y_min, y_max)
res = minimize(f2, [x0,y0], method='powell', tol=0.0001, options={'disp': True})