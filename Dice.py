import numpy as np
import scipy as sci

def dice_roll():
    roll = np.random.randint(1,7)
    return roll


def combiner():
    die_1 = dice_roll()
    die_2 = dice_roll()
    return die_1 + die_2

def collecter(N):
    twos = 0
    threes = 0
    fours = 0
    fives = 0
    sixes = 0
    sevens = 0
    eights = 0
    nines = 0
    tens = 0
    elevens = 0
    twelves = 0
    for i in range(N):
        sum = combiner()
        if sum == 2:
            twos = twos + 1
        elif sum == 3:
            threes = threes + 1
        elif sum == 4:
            fours = fours + 1
        elif sum == 5:
            fives = fives + 1
        elif sum == 6:
            sixes = sixes + 1
        elif sum == 7:
            sevens = sevens + 1
        elif sum == 8:
            eights = eights + 1
        elif sum == 9:
            nines = nines + 1
        elif sum == 10:
            tens = tens + 1
        elif sum == 11:
            elevens = elevens + 1
        elif sum == 12:
            twelves = twelves + 1
    print("Twos ", twos, ' ', (twos/N * 100), "%")
    print("Threes ", threes, ' ', (threes/N * 100), "%")
    print("Fours ", fours, ' ', (fours/N * 100), "%")
    print("Fives ", fives, ' ', (fives/N * 100), "%")
    print("Sixes ", sixes, ' ', (sixes/N * 100), "%")
    print("Sevens ", sevens, ' ', (sevens/N * 100), "%")
    print("Eights ", eights, ' ', (eights/N * 100), "%")
    print("Nines ", nines, ' ', (nines/N * 100), "%")
    print("Tens ", tens, ' ', (tens/N * 100), "%")
    print("Elevens ", elevens, ' ', (elevens/N * 100), "%")
    print("Twelves ", twelves, ' ', (twelves/N * 100), "%")
collecter(100000)