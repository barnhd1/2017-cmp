import random
import numpy as np
import matplotlib.pyplot as plt

def f2(x,y):
    return 1/2*x**2 + 1/4*y**2

def monte(N):
    size_x = 4
    size_y = 4
    xcoor = 0
    ycoor = 0
    minNum = 999999         
    for x in range(N):
        y = (random.random()*size_x - size_x / 2)
        x = (random.random()*size_y - size_y / 2)
        
        z = f2(x,y)
        if z < minNum:
            minNum = z
            xcoor = x
            ycoor = y
    print(minNum, 'at x = ', xcoor, ' y = ', ycoor)

monte(100000)