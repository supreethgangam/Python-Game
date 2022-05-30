import numpy as np
from constants import *
import colorama
from colorama import Fore,Back,Style
colorama.init(autoreset=True)

col = Back.MAGENTA + Fore.BLACK + Style.BRIGHT

#f = open("grid.txt","a")

class Townhall(Building):
    def __init__(self,x,y):
        super().__init__(x,y,twnhall_hgt,twnhall_wdt,twnhall_health,twnhall_health,"townhall")
    
class Hut(Building):
    def __init__(self,x,y):
        super().__init__(x,y,hut_hgt,hut_wdt,hut_health,hut_health,"hut")

class Wall(Building):
    def __init__(self,x,y):
        super().__init__(x,y,wall_hgt,wall_wdt,wall_health,wall_health,"wall")

class Cannon(Building):
    def __init__(self,x,y):
        super().__init__(x,y,cannon_hgt,cannon_wdt,cannon_health,cannon_health,"cannon")        
        self.range = 6
        self.dmg = 10
        self.atck = 0

    def attack(self,arr):
        tmp = 0
        for i in arr:
            if i.health > 0 and i.type != "balloon":
                dist = (i.x-self.x)**2 + (i.y-self.y)**2
                #print(dist,(self.range)**2,i.health)
                if dist <= (self.range)**2:
                    #print(i.x,i.y,"1")
                    i.health -= self.dmg
                    if i.health<0:
                        i.health = 0
                    i.update()
                    return 1
        return 0

class WizTower(Building):
    def __init__(self,x,y):
        super().__init__(x,y,wiz_hgt,wiz_wdt,wiz_health,wiz_health,"wiz")        
        self.range = 6
        self.dmg = 10
        self.atck = 0

    def attack(self,arr):
        tmp = 0
        for i in arr:
            if i.health > 0:
                dist = (i.x-self.x)**2 + (i.y-self.y)**2
                #print(dist,(self.range)**2,i.health)
                if dist <= (self.range)**2:
                    #print(i.x,i.y,"1")
                    for j in arr:
                        if j.health > 0:
                            temp_dist = (i.x-j.x)**2 + (i.y-j.y)**2
                            if temp_dist <= 2:
                                j.health -= self.dmg
                                if j.health<0:
                                    j.health = 0
                                j.update()
                    return 1
        return 0
                

class King():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.h = 1
        self.w = 1
        self.dir = "right"
        self.health = king_hlt
        self.maxhlt = king_hlt
        self.dmg = king_damage
        self.axe = 0
        self.type = "king"
    
    def add(self):
        grid[self.x][self.y] = col+"K"  
        grid[self.x][self.y+1] = col+">"
    
    def update(self):
        if self.health <= 0:
            grid[self.x][self.y] = " "
            grid[self.x][self.y+1] = " "
        if self.axe and self.health > 0:
            grid[self.x][self.y+1] = col + "~"

    def healthbar(self):
        h1 = self.health    
        h2 = self.maxhlt
        col1 = Back.MAGENTA
        per = h1/h2
        bar=[]*52
        bar.append("|")
        for i in range(50):
            if i <= 50*per:
                bar.append(col1+"/")
            else:
                bar.append(".")
        bar.append("|")
        for i in range(len(bar)):
            print(bar[i],end="")
        print("\n")

    def damage(self,d):
        self.health = self.health - d
    
    def move(self,inp):
        
        if inp == "W" and self.x - 1 >= 0 and self.y+1 <= m-1:
            if self.dir == "up":
                if grid[self.x-1][self.y] == " " and grid[self.x-1][self.y+1] == " ":
                    grid[self.x][self.y] = " "
                    grid[self.x][self.y+1] = " "
                    self.x = self.x - 1
                    grid[self.x][self.y] = col+"K"
                    grid[self.x][self.y+1] = col+"^"
            else:
                self.dir = "up"
                grid[self.x][self.y+1] = col+"^"

        if inp == "S" and self.x + 1 <= n-1 and self.y+1 <= m-1:
            if self.dir == "down":
                if grid[self.x+1][self.y] == " " and grid[self.x+1][self.y+1] == " ":
                    grid[self.x][self.y] = " "
                    grid[self.x][self.y+1] = " "
                    self.x = self.x + 1
                    grid[self.x][self.y] = col+"K"
                    grid[self.x][self.y+1] = col+"v"
            else:
                self.dir = "down"
                grid[self.x][self.y+1] = col+"v"

        if inp == "D" and self.y + 2 <= m-1:
            if self.dir == "right":
                if grid[self.x][self.y+2] == " ":
                    grid[self.x][self.y] = " "
                    grid[self.x][self.y+1] = " "
                    self.y = self.y + 1
                    grid[self.x][self.y] = col+"K"
                    grid[self.x][self.y+1] = col+">"
            else:
                self.dir = "right"
                grid[self.x][self.y+1] = col+">"
        
        if inp == "A" and self.y - 1 >= 0:
            if self.dir == "left":
                if grid[self.x][self.y-1] == " ":
                    grid[self.x][self.y] = " "
                    grid[self.x][self.y+1] = " "
                    self.y = self.y - 1
                    grid[self.x][self.y] = col+"K"
                    grid[self.x][self.y+1] = col+"<"
            else:
                self.dir = "left"
                grid[self.x][self.y+1] = col+"<"
                

    def attack(self,inp,arr):
        if inp == " ":
            if self.dir == "right":
                for i in arr:
                    if self.y+2 == i.y and self.x >= i.x and self.x < i.x+i.h and i.health > 0:
                        i.health -= self.dmg
                        if i.health < 0:
                            i.health = 0
                        i.update()
                        
            if self.dir == "left":
                for i in arr:
                    
                    if self.y-1 == i.y+i.w-1 and self.x >= i.x and self.x < i.x+i.h and i.health > 0:
                        i.health -= self.dmg
                        if i.health < 0:
                            i.health = 0
                        i.update()
                        
            if self.dir == "up":
                for i in arr:
                    if self.x-1 == i.x+i.h-1 and self.y >= i.y and self.y < i.y+i.w and i.health > 0:
                        i.health -= self.dmg
                        if i.health < 0:
                            i.health = 0
                        i.update()
                        
            if self.dir == "down":
                for i in arr:
                    if self.x+1 == i.x and self.y >= i.y and self.y < i.y+i.w and i.health > 0:
                        i.health -= self.dmg
                        if i.health < 0:
                            i.health = 0
                        i.update()
                        
        
    def axe_move(self,inp):
        if inp == "W" and self.x - 1 >= 0 and self.y+1 <= m-1:
            if grid[self.x-1][self.y] == " " and grid[self.x-1][self.y+1] == " ":
                grid[self.x][self.y] = " "
                grid[self.x][self.y+1] = " "
                self.x = self.x - 1
                grid[self.x][self.y] = col+"K"
                grid[self.x][self.y+1] = col+"~"

        if inp == "S" and self.x + 1 <= n-1 and self.y+1 <= m-1:
            if grid[self.x+1][self.y] == " " and grid[self.x+1][self.y+1] == " ":
                grid[self.x][self.y] = " "
                grid[self.x][self.y+1] = " "
                self.x = self.x + 1
                grid[self.x][self.y] = col+"K"
                grid[self.x][self.y+1] = col+"~"

        if inp == "D" and self.y + 2 <= m-1:
            if grid[self.x][self.y+2] == " ":
                grid[self.x][self.y] = " "
                grid[self.x][self.y+1] = " "
                self.y = self.y + 1
                grid[self.x][self.y] = col+"K"
                grid[self.x][self.y+1] = col+"~"
            
        if inp == "A" and self.y - 1 >= 0:
            if grid[self.x][self.y-1] == " ":
                grid[self.x][self.y] = " "
                grid[self.x][self.y+1] = " "
                self.y = self.y - 1
                grid[self.x][self.y] = col+"K"
                grid[self.x][self.y+1] = col+"~"

    def axe_attack(self,inp,arr):
            if inp == " ":
                for i in arr:
                    dis = (i.x-self.x)**2 + (i.y-self.y)**2
                    if dis < 25:
                        i.health -= self.dmg
                        if i.health < 0:
                            i.health = 0
                        i.update()

class Queen():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.h = 1
        self.w = 1
        self.dir = "right"
        self.health = king_hlt
        self.maxhlt = king_hlt
        self.dmg = king_damage-1
        self.axe = 0
        self.type = "queen"
    
    def add(self):
        grid[self.x][self.y] = col+"Q"  
        grid[self.x][self.y+1] = col+">"
    
    def update(self):
        if self.health <= 0:
            grid[self.x][self.y] = " "
            grid[self.x][self.y+1] = " "
        if self.axe and self.health > 0:
            grid[self.x][self.y+1] = col + "~"

    def healthbar(self):
        h1 = self.health    
        h2 = self.maxhlt
        col1 = Back.MAGENTA
        per = h1/h2
        bar=[]*52
        bar.append("|")
        for i in range(50):
            if i <= 50*per:
                bar.append(col1+"/")
            else:
                bar.append(".")
        bar.append("|")
        for i in range(len(bar)):
            print(bar[i],end="")
        print("\n")

    def damage(self,d):
        self.health = self.health - d
    
    def move(self,inp):
        
        if inp == "W" and self.x - 1 >= 0 and self.y+1 <= m-1:
            if self.dir == "up":
                if grid[self.x-1][self.y] == " " and grid[self.x-1][self.y+1] == " ":
                    grid[self.x][self.y] = " "
                    grid[self.x][self.y+1] = " "
                    self.x = self.x - 1
                    grid[self.x][self.y] = col+"Q"
                    grid[self.x][self.y+1] = col+"^"
            else:
                self.dir = "up"
                grid[self.x][self.y+1] = col+"^"

        if inp == "S" and self.x + 1 <= n-1 and self.y+1 <= m-1:
            if self.dir == "down":
                if grid[self.x+1][self.y] == " " and grid[self.x+1][self.y+1] == " ":
                    grid[self.x][self.y] = " "
                    grid[self.x][self.y+1] = " "
                    self.x = self.x + 1
                    grid[self.x][self.y] = col+"Q"
                    grid[self.x][self.y+1] = col+"v"
            else:
                self.dir = "down"
                grid[self.x][self.y+1] = col+"v"

        if inp == "D" and self.y + 2 <= m-1:
            if self.dir == "right":
                if grid[self.x][self.y+2] == " ":
                    grid[self.x][self.y] = " "
                    grid[self.x][self.y+1] = " "
                    self.y = self.y + 1
                    grid[self.x][self.y] = col+"Q"
                    grid[self.x][self.y+1] = col+">"
            else:
                self.dir = "right"
                grid[self.x][self.y+1] = col+">"
        
        if inp == "A" and self.y - 1 >= 0:
            if self.dir == "left":
                if grid[self.x][self.y-1] == " ":
                    grid[self.x][self.y] = " "
                    grid[self.x][self.y+1] = " "
                    self.y = self.y - 1
                    grid[self.x][self.y] = col+"Q"
                    grid[self.x][self.y+1] = col+"<"
            else:
                self.dir = "left"
                grid[self.x][self.y+1] = col+"<"
                

    def attack(self,inp,arr):
        if inp == " ":
            if self.dir == "right":
                pos_x = self.x
                pos_y = self.y+8
                for i in arr:
                    dist = (i.x-pos_x)**2 + (i.y-pos_y)**2
                    if dist <= 8:
                        i.health -= self.dmg
                        if i.health < 0:
                            i.health = 0
                        i.update()
                        
            if self.dir == "left":
                pos_x = self.x
                pos_y = self.y-8
                for i in arr:
                    dist = (i.x-pos_x)**2 + (i.y-pos_y)**2
                    if dist <= 8:
                        i.health -= self.dmg
                        if i.health < 0:
                            i.health = 0
                        i.update()
                        
            if self.dir == "up":
                pos_x = self.x-8
                pos_y = self.y
                for i in arr:
                    dist = (i.x-pos_x)**2 + (i.y-pos_y)**2
                    if dist <= 8:
                        i.health -= self.dmg
                        if i.health < 0:
                            i.health = 0
                        i.update()
                        
            if self.dir == "down":
                pos_x = self.x+8
                pos_y = self.y
                for i in arr:
                    dist = (i.x-pos_x)**2 + (i.y-pos_y)**2
                    if dist <= 8:
                        i.health -= self.dmg
                        if i.health < 0:
                            i.health = 0
                        i.update()
                        
        
    def axe_move(self,inp):
        if inp == "W" and self.x - 1 >= 0 and self.y+1 <= m-1:
            if grid[self.x-1][self.y] == " " and grid[self.x-1][self.y+1] == " ":
                grid[self.x][self.y] = " "
                grid[self.x][self.y+1] = " "
                self.x = self.x - 1
                grid[self.x][self.y] = col+"Q"
                grid[self.x][self.y+1] = col+"~"

        if inp == "S" and self.x + 1 <= n-1 and self.y+1 <= m-1:
            if grid[self.x+1][self.y] == " " and grid[self.x+1][self.y+1] == " ":
                grid[self.x][self.y] = " "
                grid[self.x][self.y+1] = " "
                self.x = self.x + 1
                grid[self.x][self.y] = col+"Q"
                grid[self.x][self.y+1] = col+"~"

        if inp == "D" and self.y + 2 <= m-1:
            if grid[self.x][self.y+2] == " ":
                grid[self.x][self.y] = " "
                grid[self.x][self.y+1] = " "
                self.y = self.y + 1
                grid[self.x][self.y] = col+"Q"
                grid[self.x][self.y+1] = col+"~"
            
        if inp == "A" and self.y - 1 >= 0:
            if grid[self.x][self.y-1] == " ":
                grid[self.x][self.y] = " "
                grid[self.x][self.y+1] = " "
                self.y = self.y - 1
                grid[self.x][self.y] = col+"Q"
                grid[self.x][self.y+1] = col+"~"

    def axe_attack(self,inp,arr):
            if inp == " ":
                if self.dir == "right":
                    pos_x = self.x
                    pos_y = self.y+16
                    for i in arr:
                        dist = (i.x-pos_x)**2 + (i.y-pos_y)**2
                        if dist <= 32:
                            i.health -= self.dmg
                            if i.health < 0:
                                i.health = 0
                            i.update()
                        
                if self.dir == "left":
                    pos_x = self.x
                    pos_y = self.y-16
                    for i in arr:
                        dist = (i.x-pos_x)**2 + (i.y-pos_y)**2
                        if dist <= 32:
                            i.health -= self.dmg
                            if i.health < 0:
                                i.health = 0
                            i.update()
                            
                if self.dir == "up":
                    pos_x = self.x-16
                    pos_y = self.y
                    for i in arr:
                        dist = (i.x-pos_x)**2 + (i.y-pos_y)**2
                        if dist <= 32:
                            i.health -= self.dmg
                            if i.health < 0:
                                i.health = 0
                            i.update()
                            
                if self.dir == "down":
                    pos_x = self.x+16
                    pos_y = self.y
                    for i in arr:
                        dist = (i.x-pos_x)**2 + (i.y-pos_y)**2
                        if dist <= 32:
                            i.health -= self.dmg
                            if i.health < 0:
                                i.health = 0
                            i.update()
            

def minimum(ins,arr):
        min = 100000
        num = 0
        iter = -1
        for i in arr:
            if i.type != "wall" and i.health>0:
                dis = (i.x-ins.x)**2 + (i.y-ins.y)**2
                if dis < min:
                    min = dis
                    iter = num
            num += 1
        if iter != -1:
            return arr[iter]

def barb_move(self,inp):

        self.move = 0

        if inp == "W" and self.x - 1 >= 0 and self.y+1 <= m-1:
            if grid[self.x-1][self.y] == " ":
                grid[self.x][self.y] = " "
                self.x = self.x - 1
                grid[self.x][self.y] = col+"B"
                self.move = 1


        if inp == "S" and self.x + 1 <= n-1 and self.y+1 <= m-1:
            if grid[self.x+1][self.y] == " ":
                grid[self.x][self.y] = " "
                self.x = self.x + 1
                grid[self.x][self.y] = col+"B"
                self.move = 1


        if inp == "D" and self.y + 1 <= m-1:
            if grid[self.x][self.y+1] == " ":
                grid[self.x][self.y] = " "
                self.y = self.y + 1
                grid[self.x][self.y] = col+"B"
                self.move = 1

        
        if inp == "A" and self.y - 1 >= 0:
            if grid[self.x][self.y-1] == " ":
                grid[self.x][self.y] = " "
                self.y = self.y - 1
                grid[self.x][self.y] = col+"B"
                self.move = 1

class Barbarian():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.h = 1
        self.w = 1
        self.health = 40
        self.maxhlt = 40
        self.dmg = barb_dmg
        self.move = 1
        self.type = "barb"

    def add(self):
        grid[self.x][self.y] = col+"B"  

    def damage(self,d):
        self.health = self.health - d    
            
    def update(self):
        col_b = Back.MAGENTA + Fore.BLACK + Style.DIM
        col_b1 = Back.MAGENTA + Fore.BLACK
        if self.health/self.maxhlt <= 0.4:
            grid[self.x][self.y] = col_b + "B"
        if self.health/self.maxhlt > 0.4 and self.health/self.maxhlt <= 0.8:
            grid[self.x][self.y] = col_b1 + "B"
        if self.health/self.maxhlt > 0.8:
            grid[self.x][self.y] = col + "B"
        if self.health <= 0:
            grid[self.x][self.y] = " "
        

    def attack(self,arr):
        obj = minimum(self,arr)
        fg=1
        
        if obj != None and self.health>0:

            if self.x < obj.x and fg:
                if obj.x != self.x:
                    barb_move(self,"S")
                    fg=0
                    if self.move == 0:
                        for i in arr:
                            if self.x+1 == i.x and self.y >= i.y and self.y < i.y+i.w:
                                if i.health:
                                    i.health = i.health - self.dmg
                                    if i.health<0:
                                        i.health = 0
                                    i.update()


            if self.y < obj.y and fg:
                if obj.y != self.y:
                    barb_move(self,"D")
                    fg=0
                    if self.move == 0:
                        for i in arr:
                            if self.y+1 == i.y and self.x >= i.x and self.x < i.x+i.h:
                                if i.health:
                                    i.health = i.health - self.dmg
                                    if i.health<0:
                                        i.health = 0
                                    i.update()

                                    
            
            if self.x > obj.x+obj.h-1 and fg:
                if obj.x+obj.h-1 != self.x:
                    barb_move(self,"W")
                    fg=0
                    if self.move == 0:
                        for i in arr:
                            if self.x == i.x+i.h and self.y >= i.y and self.y < i.y+i.w:
                                if i.health:
                                    i.health = i.health - self.dmg
                                    if i.health<0:
                                        i.health = 0
                                    i.update()
                                    
            
            if self.y > obj.y+obj.w-1 and fg:
                if obj.y+obj.w-1 != self.y:
                    barb_move(self,"A")
                    fg=0
                    if self.move == 0:
                        for i in arr:
                            if self.y == i.y+i.w and self.x >= i.x and self.x < i.x+i.h:
                                if i.health:
                                    i.health = i.health - self.dmg
                                    if i.health<0:
                                        i.health = 0
                                i.update()

def minimum1(ins,arr):
        min = 100000
        num = 0
        iter = -1
        for i in arr:
            if (i.type == "cannon" or i.type == "wiz") and i.health>0:
                dis = (i.x-ins.x)**2 + (i.y-ins.y)**2
                if dis < min:
                    min = dis
                    iter = num
            num += 1
        if iter != -1:
            return arr[iter]
        min = 100000
        num = 0
        for i in arr:
            if i.type != "wall" and i.health>0:
                dis = (i.x-ins.x)**2 + (i.y-ins.y)**2
                if dis < min:
                    min = dis
                    iter = num
            num += 1
        if iter != -1:
            return arr[iter]

def balloon_move(self,inp,arr,spd):

        if inp == "W" and self.x - spd >= 0 and self.y+spd <= m-1:
            grid[self.x][self.y] = " "
            for i in arr:
                if i.health > 0:
                    if self.x >= i.x and self.x <= i.x+i.h-1: 
                        if self.y >= i.y and self.y <= i.y+i.w-1:
                            i.update()
            self.x = self.x - spd
            grid[self.x][self.y] = col+"0"


        if inp == "S" and self.x + spd <= n-1 and self.y+spd <= m-1:
            grid[self.x][self.y] = " "
            for i in arr:
                if i.health > 0:
                    if self.x >= i.x and self.x <= i.x+i.h-1: 
                        if self.y >= i.y and self.y <= i.y+i.w-1:
                            i.update()
            self.x = self.x + spd
            grid[self.x][self.y] = col+"0"

        if inp == "D" and self.y + spd <= m-1:
            grid[self.x][self.y] = " "
            for i in arr:
                if i.health > 0:
                    if self.x >= i.x and self.x <= i.x+i.h-1: 
                        if self.y >= i.y and self.y <= i.y+i.w-1:
                            i.update()
            self.y = self.y + spd
            grid[self.x][self.y] = col+"0"
        
        if inp == "A" and self.y - spd >= 0:
            grid[self.x][self.y] = " "
            for i in arr:
                if i.health > 0:
                    if self.x >= i.x and self.x <= i.x+i.h-1: 
                        if self.y >= i.y and self.y <= i.y+i.w-1:
                            i.update()
            self.y = self.y - spd
            grid[self.x][self.y] = col+"0"

class Balloon():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.h = 1
        self.w = 1
        self.health = 40
        self.maxhlt = 40
        self.dmg = 2*barb_dmg
        self.type = "balloon"

    def add(self):
        grid[self.x][self.y] = col+"0"  

    def damage(self,d):
        self.health = self.health - d    
            
    def update(self):
        col_b = Back.MAGENTA + Fore.BLACK + Style.DIM
        col_b1 = Back.MAGENTA + Fore.BLACK
        if self.health/self.maxhlt <= 0.4:
            grid[self.x][self.y] = col_b + "0"
        if self.health/self.maxhlt > 0.4 and self.health/self.maxhlt <= 0.8:
            grid[self.x][self.y] = col_b1 + "0"
        if self.health/self.maxhlt > 0.8:
            grid[self.x][self.y] = col + "0"
        if self.health <= 0:
            grid[self.x][self.y] = " "
        

    def attack(self,arr):
        obj = minimum1(self,arr)
        fg = 1

        if obj != None and self.health>0:

            if self.x < obj.x and fg:
                if self.x == obj.x-1:
                    balloon_move(self,"S",arr,1)
                    fg=0
                if obj.x != self.x and fg:
                    balloon_move(self,"S",arr,2)
                    fg=0

            if self.y < obj.y and fg:
                if self.y == obj.y-1:
                    balloon_move(self,"D",arr,1)
                    fg=0
                if obj.y != self.y and fg:
                    balloon_move(self,"D",arr,2)
                    fg=0
            
            if self.x > obj.x+obj.h-1 and fg:
                if self.x == obj.x+obj.h:
                    balloon_move(self,"W",arr,1)
                    fg=0
                if obj.x+obj.h-1 != self.x and fg:
                    balloon_move(self,"W",arr,2)
                    fg=0

            if self.y > obj.y+obj.w-1 and fg:
                if self.y == obj.y+obj.w:
                    balloon_move(self,"A",arr,1)
                    fg=0
                if obj.y+obj.w-1 != self.y and fg:
                    balloon_move(self,"A",arr,2)
                    fg=0

            if (self.x >= obj.x and self.x <= obj.x+obj.h-1) and fg:
                if self.y >= obj.y and self.y <= obj.y+obj.w-1:
                    if obj.health > 0:
                        obj.health = obj.health - self.dmg
                    if obj.health<0:
                        obj.health = 0
                    obj.update()    
        

def archer_move(self,inp,spd):

        self.move = 0

        if inp == "W" and self.x - spd >= 0 and self.y+spd <= m-1:
            if grid[self.x-spd][self.y] == " " and grid[self.x-1][self.y] == " ":
                grid[self.x][self.y] = " "
                self.x = self.x - spd
                grid[self.x][self.y] = col+"A"
                self.move = 1
            if grid[self.x-spd][self.y] != " ":
                self.move = 3
            if grid[self.x-1][self.y] != " ":
                self.move = 2

        if inp == "S" and self.x + spd <= n-1 and self.y+spd <= m-1:
            if grid[self.x+spd][self.y] == " " and grid[self.x+1][self.y] == " ":
                grid[self.x][self.y] = " "
                self.x = self.x + spd
                grid[self.x][self.y] = col+"A"
                self.move = 1
            if grid[self.x+spd][self.y] != " ":
                self.move = 3 
            if grid[self.x+1][self.y] != " ":
                self.move = 2 

        if inp == "D" and self.y + spd <= m-1:
            if grid[self.x][self.y+spd] == " " and grid[self.x][self.y+1] == " ":
                grid[self.x][self.y] = " "
                self.y = self.y + spd
                grid[self.x][self.y] = col+"A"
                self.move = 1
            if grid[self.x][self.y+spd] != " ":
                self.move = 3
            if grid[self.x][self.y+1] != " ":
                self.move = 2
        
        if inp == "A" and self.y - spd >= 0:
            if grid[self.x][self.y-spd] == " " and grid[self.x][self.y-1] == " ":
                grid[self.x][self.y] = " "
                self.y = self.y - spd
                grid[self.x][self.y] = col+"A"
                self.move = 1
            if grid[self.x][self.y-spd] != " ":
                self.move = 3
            if grid[self.x][self.y-1] != " ":
                self.move = 2

class Archer():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.h = 1
        self.w = 1
        self.health = 20
        self.maxhlt = 20
        self.dmg = archer_dmg
        self.move = 1
        self.type = "archer"
        self.range = 8

    def add(self):
        grid[self.x][self.y] = col+"A"  

    def damage(self,d):
        self.health = self.health - d    
            
    def update(self):
        col_b = Back.MAGENTA + Fore.BLACK + Style.DIM
        col_b1 = Back.MAGENTA + Fore.BLACK
        if self.health/self.maxhlt <= 0.4:
            grid[self.x][self.y] = col_b + "A"
        if self.health/self.maxhlt > 0.4 and self.health/self.maxhlt <= 0.8:
            grid[self.x][self.y] = col_b1 + "A"
        if self.health/self.maxhlt > 0.8:
            grid[self.x][self.y] = col + "A"
        if self.health <= 0:
            grid[self.x][self.y] = " "
        

    def attack(self,arr):
        obj = minimum(self,arr)
        fg=1

        if obj != None and self.health>0:

            dist = (obj.x-self.x)**2+(obj.y-self.y)**2

            if dist <= (self.range)**2:
                obj.health = obj.health - self.dmg
                if obj.health<0:
                    obj.health = 0
                obj.update()
                fg=0
            
            if self.x < obj.x and fg:
                if self.x == obj.x-1:
                    archer_move(self,"S",1)
                    fg=0
                if obj.x != self.x and fg:
                    archer_move(self,"S",2)
                    fg=0
                if self.move == 2 or self.move == 3:
                    for i in arr:
                        if i.y == self.y and i.x-(self.move-1) == self.x:
                            i.health -= self.dmg
                            if i.health<0:
                                i.health=0
                            i.update()

            if self.y < obj.y and fg:
                if self.y == obj.y-1:
                    archer_move(self,"D",1)
                    fg=0
                if obj.y != self.y and fg:
                    archer_move(self,"D",2)
                    fg=0
                if self.move == 2 or self.move == 3:
                    for i in arr:
                        if i.y-(self.move-1) == self.y and i.x == self.x:
                            i.health -= self.dmg
                            if i.health<0:
                                i.health=0
                            i.update()
            
            if self.x > obj.x+obj.h-1 and fg:
                if self.x == obj.x+obj.h:
                    archer_move(self,"W",1)
                    fg=0
                if obj.x+obj.h-1 != self.x and fg:
                    archer_move(self,"W",2)
                    fg=0
                if self.move == 2 or self.move == 3:
                    for i in arr:
                        if i.y == self.y and i.x == self.x-(self.move-1):
                            i.health -= self.dmg
                            if i.health<0:
                                i.health=0
                            i.update()

            if self.y > obj.y+obj.w-1 and fg:
                if self.y == obj.y+obj.w:
                    archer_move(self,"A",1)
                    fg=0
                if obj.y+obj.w-1 != self.y and fg:
                    archer_move(self,"A",2)
                    fg=0
                if self.move == 2 or self.move == 3:
                    for i in arr:
                        if i.y == self.y-(self.move-1) and i.x == self.x:
                            i.health -= self.dmg
                            if i.health<0:
                                i.health=0
                            i.update()

            

         

  

                                
        
        
        

        
        


            
   
  
            



            

