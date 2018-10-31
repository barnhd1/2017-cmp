import numpy as np
from vpython import *
import matplotlib.pyplot as plt

L1 = 101
L2 = 101
moves = 10000
def game():
    posx = 50
    posy = 50

    xmoves = []
    ymoves = []
    for i in range(moves):
        move = np.random.randint(1,5)
        if move == 1:
            if posx >= L1:
                continue
            posx += 1
        elif move == 2:
            if posx <= 0:
                continue
            posx -= 1
        elif move == 3:
            if posy >= L2:
                continue
            posy += 1
        elif move == 4:
            if posy <= 0:
                continue
            posy -= 1
        xmoves.append(posx)
        ymoves.append(posy)
    background = canvas(title='Examples of Brownian Motion',
         width=700, height=700,
         center=vector(50,50,0), background=color.red)
    s = sphere(pos=vector(50,50,0),radius=5,color=color.blue, make_trail = True)

    for i in range(moves):
        rate(190)
        x = xmoves[i]
        y = ymoves[i]
        s.pos = vector(x,y,0)
    plt.plot(xmoves,ymoves, '-')
    plt.show()

game()