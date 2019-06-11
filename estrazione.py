#!/usr/bin/env python3

import sys
import math
import random

if(len(sys.argv) > 1):
    players = int(sys.argv[1])
    middle = math.floor(players/2) + 1

    if(players%2 == 0):
        first = list(range(1,middle))
        second = list(range(middle,players+1))
        match = []

        for i in range(middle-1):
            first_choose = random.choice(first)
            second_choose = random.choice(second)
            match.append((first_choose, second_choose))
            first.remove(first_choose)
            second.remove(second_choose)
        
        print(match)
    
    else:
        print("Il numero di giocatori deve essere pari!")

else:
    print("Inserire il numero di giocatori!")

