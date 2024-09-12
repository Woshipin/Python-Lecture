from random import *
import random

class Bingo: 
    def generate_number(self, minimum, maximum, numberlist, draw_length=5):        
        while len(numberlist) < draw_length:
            randos = randint(minimum, maximum)
        
            if randos not in numberlist:
                numberlist.append(randos)
                
    def print_tile(self, bnumber, inumber, nnumber, gnumber, onumber):
        i = 0
        print(" B  I  N  G  O")
        while i < 5:
            if i == 2:
                print('{:2d}'.format(bnumber[i]), inumber[i], "  ", gnumber[i], onumber[i])
            else:
                print('{:2d}'.format(bnumber[i]), inumber[i], nnumber[i], gnumber[i], onumber[i])
            i += 1
            
    def draw_bingo(self):
        alphabets = ['B', 'I', 'N', 'G', 'O']
        randalp = random.choices(alphabets)[0]
        
        match randalp:
            case 'B':
                randnum = randint(1, 20)
            case 'I':
                randnum = randint(21, 40)
            case 'N':
                randnum = randint(41, 60)
            case 'G':
                randnum = randint(61, 80)
            case 'O':
                randnum = randint(81, 90)
                
        print("Current Draw: ", randalp, randnum)
    