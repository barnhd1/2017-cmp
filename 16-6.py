import numpy as np


def f5(x):
    return (1/2 * x[0] ** 2 + 1/3 * x[1] ** 2 - 1/4 * x[1] * x[0])


def min_search(N):
    x_min, x_max = -4, 4
    y_min, y_max = -4, 4                   
    minf = f5([x_min,y_min])
    minNum = 99999999999999
    xcoor = 0
    ycoor = 0

    x = np.linspace(x_min,x_max,N)
    y = np.linspace(y_min,y_max,N)

    for i in x:
        for j in y:
            if f5([i,j]) < minNum:
                xcoor = i
                ycoor = j
                minNum = f5([i,j])

    
    print(minNum, 'at x = ', xcoor, ' y = ', ycoor)


min_search(1000)