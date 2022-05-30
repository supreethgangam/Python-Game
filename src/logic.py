from constants import *
from create import *
from input import *
from base import *

import os
import sys
import time
  
path = os.path.realpath(__file__)
dir = os.path.dirname(path)
dir = dir.replace('src', 'replays')
os.chdir(dir)

os.system("stty -echo")
# sys.stdout.write("\033[?25l")
# sys.stdout.flush()

base = Base()
base.initialize()

def check(buildings,troops,level):
    fg = 0
    fg1 = 0
    for i in buildings:
        if i.health != 0 and i.type != "wall":
            fg = 1
    for i in troops:
        if i.health != 0:
            fg1 = 1
    if fg==0 and level==1:
        # level=2
        base.level2()
        return 2
    if fg==0 and level==2:
        # level=3
        base.level3()
        return 3
    if fg==0 and level==3:
        print("!!!!!WIN!!!!!")
        return 0
    if fg1==0:
        print("!!!!!LOSE!!!!!")
        return 0
    return 1

class Logic:
    
    def start_game(self):
        t = 0
        inputs = []
        level = 1
        start_time = 0
        print("Choose King(K) or Queen(Q): ")
        inp = input()
        if inp == "Q":
            base.hero = 1
        base.initialize_hero()  
        while 1:
            # sys.stdin.flush()
            # sys.stdout.flush()
            os.system("clear")
            base.obj3.healthbar()
            # print("LEVEL: 1\n")
            for i in base.troops:
                if i.type == "balloon" and i.health>0:
                    i.update()
            show()
            flag=check(base.buildings,base.troops,level)
            if flag!=0 and flag!=1:
                level=flag
            if flag==0:
                with open('inputs.txt','w') as f:
                    for i in inputs:
                        f.write(i)
                break
            getch = Get()
            inp=input_to(getch)
            if inp == "X":
                base.obj3.axe = 1
                base.obj3.update()
                start_time = time.time()
                #f.write(grid)
                #f.write("\n")
            if base.obj3.health>0 and base.obj3.axe == 0:
                base.obj3.move(inp)
                base.obj3.attack(inp,base.buildings)
            if base.obj3.health>0 and base.obj3.axe != 0 and (time.time()-start_time>1):
                base.obj3.axe_move(inp)
                base.obj3.axe_attack(inp,base.buildings)
                start_time=0
            if inp == "C":
                base.spawn1()
                #f.write(grid)
                #f.write("\n")
            if inp == "V":
                base.spawn2()
                #f.write(grid)
                #f.write("\n")
            if inp == "B":
                base.spawn3()
                #f.write(grid)
                #f.write("\n")
            if inp == "J":
                base.spawn4()
            if inp == "K":
                base.spawn5()
            if inp == "L":
                base.spawn6()
            if inp == "I":
                base.spawn7()
            if inp == "O":
                base.spawn8()
            if inp == "P":
                base.spawn9()
            if inp == "H":
                for i in base.troops:
                    i.health = min(i.health*1.5,i.maxhlt)
                    i.update()
            if inp == "T" and t==0:
                for i in base.buildings:
                    if i.type == "cannon":
                        t=1
                        i.health = i.health/2
                        i.update() 
            if inp != None:
                inputs.append(inp)
                for i in base.troops:
                    if i.type == "barb" and i.health > 0:
                        i.attack(base.buildings)
                    if i.type == "balloon" and i.health>0:
                        i.attack(base.buildings)
                    if i.type == "archer" and i.health>0:
                        i.attack(base.buildings)
                for i in base.defense:
                    if i.health > 0:
                        out = i.attack(base.troops)
                        if out:
                            i.atck = 1
                        else:
                            i.atck = 0
                        i.update()
                # if base.obj5.health > 0:
                #     out=base.obj5.attack(base.troops)
                #     if out:
                #         base.obj5.atck = 1
                #     else:
                #         base.obj5.atck = 0
                #     base.obj5.update()
                # if base.obj6.health > 0:
                #     out=base.obj6.attack(base.troops)
                #     if out:
                #         base.obj6.atck = 1
                #     else:
                #         base.obj6.atck = 0
                #     base.obj6.update()
            if inp == "Q":
                break

os.system("stty -echo")
# sys.stdout.write("\033[?25h")
# sys.stdout.flush()