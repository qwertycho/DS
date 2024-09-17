#!/usr/bin/python3
import shutil
import math
import random

class Dobbelsteen:
    '''
    Minimale abstractie bovenop random
    '''
    __numbers = []

    def __init__(self, sides = 6) -> None:
        if sides < 4:
            raise Exception("Invalid number of sides")
        
        self.__numbers = []
        #zijdes aanmaken
        for i in range(1, sides+1):
            self.__numbers.append(i)
        
    def roll(self):
        #shuffle gebruiken om aan de opdracht te voldoen
        random.shuffle(self.__numbers)
        return self.__numbers[0]

dobbelsteen_zijdes = int(input("Hoeveel zijdes moeten de dobbelstenen hebben (min 4): "))
throw_amount = int(input("Hoe vaak wil je gooien: "))

dobbelsteen_1 = Dobbelsteen(dobbelsteen_zijdes)
dobbelsteen_2 = Dobbelsteen(dobbelsteen_zijdes)

throws = {}

for i in range(throw_amount):
    sum = dobbelsteen_1.roll() + dobbelsteen_2.roll()
    if sum in throws:
        throws[sum] = throws[sum]+1
    else:
        throws[sum] = 1

#zijwaartse normaaldistributie
#te lui om het te kantelen
terminal = shutil.get_terminal_size()

# throw dict sorteren op key (sum) zodat deze netjes gepresenteerd kan worden 
# i.p.v. op de volgorde van insertion
for throw in sorted(throws.items()):
    number = throw[0]
    count = throw[1]
    # het aantal # normaliseren naar % van de terminal breedte zodat deze nooit over kan lopen
    normalised = math.ceil((count/throw_amount) * (terminal.columns/2))
    print(f"{throw[0]:<4}: {throw[1]:<5} | {'#' * normalised}")

#De dobbelstenen maken een normaaldistributie
# omdat zijdes[n] + zijdes[-n] = middelste waarde
# Voor een dobbelsteen met 6 zijdes:
# 1 + 6 = 7
# 2 + 5 = 7
# 3 + 4 = 7
# etc