from random import *

class Lottery:
    def generate_number(self, minimum=1, maximum=10, draw_length=5):
        lottery_num = []
        
        while len(lottery_num) < draw_length:
            randos = randint(minimum, maximum)
        
            if randos not in lottery_num:
                lottery_num.append(randos)
                
        return lottery_num