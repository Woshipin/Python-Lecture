from random import *
import random

class Bingo: 
    # 生成随机号码的函数，参数为最小值、最大值、号码列表以及抽取的长度（默认为5）
    def generate_number(self, minimum, maximum, numberlist, draw_length=5):        
        while len(numberlist) < draw_length:
            # 在指定范围内随机生成一个数字
            randos = randint(minimum, maximum)
        
            # 如果生成的数字不在号码列表中，才将其添加到列表中
            if randos not in numberlist:
                numberlist.append(randos)
    
    # 打印BINGO卡片，参数为5列号码（B, I, N, G, O）
    def print_tile(self, bnumber, inumber, nnumber, gnumber, onumber):
        i = 0
        # 打印表头 "B  I  N  G  O"
        print(" B  I  N  G  O")
        while i < 5:
            # 如果是第三行（即索引为2的行），在N列打印空格（常见BINGO卡片的格式）
            if i == 2:
                print('{:2d}'.format(bnumber[i]), inumber[i], "  ", gnumber[i], onumber[i])
            else:
                # 打印每一列的数字
                print('{:2d}'.format(bnumber[i]), inumber[i], nnumber[i], gnumber[i], onumber[i])
            i += 1
    
    # 随机抽取一个BINGO号码
    def draw_bingo(self):
        # 字母列表，分别对应BINGO五个字母
        alphabets = ['B', 'I', 'N', 'G', 'O']
        # 随机选择一个字母
        randalp = random.choices(alphabets)[0]
        
        # 根据抽到的字母，生成不同范围的随机号码
        match randalp:
            case 'B':
                randnum = randint(1, 20)  # B列号码范围为1到20
            case 'I':
                randnum = randint(21, 40)  # I列号码范围为21到40
            case 'N':
                randnum = randint(41, 60)  # N列号码范围为41到60
            case 'G':
                randnum = randint(61, 80)  # G列号码范围为61到80
            case 'O':
                randnum = randint(81, 90)  # O列号码范围为81到90
                
        # 打印当前抽到的字母和号码
        print("Current Draw: ", randalp, randnum)
