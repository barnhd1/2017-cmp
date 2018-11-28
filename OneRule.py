from sklearn.datasets import load_iris
from collections import OrderedDict
import pandas as pd
import matplotlib.pyplot as plt

from pandas.tools.plotting import scatter_matrix


dataset = load_iris()
X = dataset.data
Y = dataset.target




import numpy as np
X_d = np.array( X>np.mean(X), dtype='int')

Iris_data = OrderedDict({'Sepal Length ': X[:,0],
             'Sepal Width': X[:,1],
             'Petal Length': X[:,2],
             'Petal Width': X[:,3],
             'Label': Y})

df = pd.DataFrame(Iris_data)

def Sepal_Length():
    f1 = 0
    f2 = 0
    f3 = 0
    total = 0
    for i in range(150):
        if X_d[:,0][i] == 1:
            if Y[i] == 0:
                f1 += 1
            elif Y[i] == 1:
                f2 += 1
            elif Y[i] == 2:
                f3 += 1
        total += 1

    return f1, f2, f3, total

#print(Sepal_Length())

def Sepal_Width():
    f1 = 0
    f2 = 0
    f3 = 0
    total = 0
    for i in range(150):
        if X_d[:,1][i] == 1:
            if Y[i] == 0:
                f1 += 1
            elif Y[i] == 1:
                f2 += 1
            elif Y[i] == 2:
                f3 += 1
        total += 1

    return f1, f2, f3, total

#print(Sepal_Width())

def Petal_Length():
    f1 = 0
    f2 = 0
    f3 = 0
    total = 0
    for i in range(150):
        if X_d[:,2][i] == 1:
            if Y[i] == 0:
                f1 += 1
            elif Y[i] == 1:
                f2 += 1
            elif Y[i] == 2:
                f3 += 1
        total += 1

    return f1, f2, f3, total

#print(Petal_Length())

def Petal_Width():
    f1 = 0
    f2 = 0
    f3 = 0
    total = 0
    for i in range(150):
        if X_d[:,3][i] == 1:
            if Y[i] == 0:
                f1 += 1
            elif Y[i] == 1:
                f2 += 1
            elif Y[i] == 2:
                f3 += 1
        total += 1

    return f1, f2, f3, total

#print(Petal_Width())

def Error():
    sl_f1, sl_f2, sl_f3, sl_total = Sepal_Length()
    sw_f1, sw_f2, sw_f3, sw_total = Sepal_Width()
    pl_f1, pl_f2, pl_f3, pl_total = Petal_Length()
    pw_f1, pw_f2, pw_f3, pw_total = Petal_Width()

    print("Sepal Length:")
    print("Flower 1: ", sl_f1/50)
    print("Flower 2: ", sl_f2/50)
    print("Flower 3: ", sl_f3/50)

    print("Inaccurate Data")
    print("")
    print("Sepal Width:")
    print("Flower 1: ", sw_f1/50)
    print("Flower 2: ", sw_f2/50)
    print("Flower 3: ", sw_f3/50)
    print("")

    print("Petal Length:")
    print("Flower 1: ", pl_f1/50)
    print("Flower 2: ", pl_f2/50)
    print("Flower 3: ", pl_f3/50)
    print("")

    print("Petal Width:")
    print("Flower 1: ", pw_f1/50)
    print("Flower 2: ", pw_f2/50)
    print("Flower 3: ", pw_f3/50)
    print("Inaccurate Data")

Error()

