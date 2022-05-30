import os
import sys
import numpy as np
import colorama
from colorama import Fore,Back,Style
colorama.init(autoreset=True)

col1 = Back.GREEN + Fore.BLACK
col2 = Back.YELLOW + Fore.BLACK
col3 = Back.RED + Fore.BLACK
col_border = Back.WHITE

m = 100
n = 30

twnhall_health = 200
twnhall_hgt = 4
twnhall_wdt = 3

hut_health = 50
hut_hgt = 2
hut_wdt = 2


wall_health = 30
wall_hgt = 1
wall_wdt = 1

cannon_health = 50
cannon_hgt = 1
cannon_wdt = 3

wiz_health = 50
wiz_hgt = 1
wiz_wdt = 3

king_hlt = 100
king_damage = 5

barb_dmg = 4
archer_dmg = 2

grid = []

for i in range(n):
    temp = []
    for j in range(m):
        temp.append(" ")
    grid.append(temp)

def show():
    #os.system("clear")
    for i in range(n):
        grid[i][m-1] = col_border+" "
        grid[i][0] = col_border+" "
    
    for j in range(m):
        grid[n-1][j] = col_border+" "
        grid[0][j] = col_border+" "

    var = ""
    for i in range(n):
        for j in range(m):
            sys.stdout.write(grid[i][j])
        sys.stdout.write("\n")

#def replay():
#    for i in range(n):
#        for j in range(m):
#           f.write(grid[i][j])


class Building:
    def __init__(self,x,y,h,w,health,max,type):
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.health = health
        self.maxhlt = max
        self.type = type
    
    def add(self):
        ch = " "
        if self.type == "hut":
            ch = " "
        if self.type == "cannon":
            ch = "C"
        if self.type == "wall":
            ch = " "
        if self.type == "wiz":
            ch = "W"
        for i in range(self.h):
            for j in range(self.w):
                grid[self.x+i][self.y+j] = col1+ch

    def update(self):
        h1 = self.health*100
        h2 = self.maxhlt
        
        if h1/h2 < 20:
            col = col3
        if h1/h2 >= 20 and h1/h2 <= 50:
            col = col2
        if h1/h2 > 50:
            col = col1
        
        ch = " "
        if self.type == "hut":
            ch = " "
        if self.type == "cannon":
            if self.atck == 1:
                ch = "#"
            if self.atck == 0:
                ch = "C"
        if self.type == "wiz":
            if self.atck == 1:
                ch = "#"
            if self.atck == 0:
                ch = "W"
        if self.type == "wall":
            ch = " "

        for i in range(self.h):
                for j in range(self.w):
                    grid[self.x+i][self.y+j] = col+ch
        if h1 == 0:
            for i in range(self.h):
                for j in range(self.w):
                    grid[self.x+i][self.y+j] = " "
            #f.write(str(np.array(grid)))
            #f.write("\n")

    def damage(self,d):
        self.health = self.health - d



