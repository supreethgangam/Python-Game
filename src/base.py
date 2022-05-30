import numpy as np
from constants import *
from create import *
from input import *


class Base:
    
    def __init__(self):
        self.buildings = []
        self.troops = []
        self.defense = []
        self.hero = 0 
        self.obj3 = King(2,3)
        self.limit1 = 6
        self.limit2 = 6
        self.limit3 = 3
    
    def initialize_hero(self):
        if self.hero:
            self.obj3 = Queen(2,3)
            self.obj3.add()
            self.obj3.healthbar()
            #obj3.damage(50)
            self.troops.append(self.obj3)
        else:
            self.obj3.add()
            self.obj3.healthbar()
            #obj3.damage(50)
            self.troops.append(self.obj3)

    def initialize(self):

        obj=Townhall(8,8)   
        obj.add()
        self.buildings.append(obj)

        #obj.damage(190)
        #obj.update()

        obj = Hut(5,5)
        obj.add()
        self.buildings.append(obj)

        obj = Hut(9,16)
        obj.add()
        self.buildings.append(obj)

        obj = Hut(16,9)
        obj.add()
        self.buildings.append(obj)

        obj = Hut(15,6)
        obj.add()
        self.buildings.append(obj)

        obj = Hut(16,16)
        obj.add()
        self.buildings.append(obj)


        for i in range(3,20):
            obj = Wall(i,3)
            obj.add()
            self.buildings.append(obj)
            obj = Wall(i,79)
            obj.add()
            self.buildings.append(obj)

        for i in range(3,80):
            obj = Wall(3,i)
            obj.add()
            self.buildings.append(obj)
            obj = Wall(19,i)
            obj.add()
            self.buildings.append(obj)
            
        obj = Cannon(8,30)
        obj.add()
        self.buildings.append(obj)
        self.defense.append(obj)

        obj = Cannon(13,30)
        obj.add()
        self.buildings.append(obj)
        self.defense.append(obj)

        obj = WizTower(8,50)
        obj.add()
        self.buildings.append(obj)
        self.defense.append(obj)
        
        obj = WizTower(13,50)
        obj.add()
        self.buildings.append(obj)
        self.defense.append(obj)

        # self.obj5.add()
        # self.buildings.append(self.obj5)

        # self.obj6.add()
        # self.buildings.append(self.obj6)

        #obj3 = King(0,0)
        

    def spawn1(self):
        if self.limit1:
            obj4 = Barbarian(4,16)
            obj4.add()
            self.troops.append(obj4)
            self.limit1 -= 1
    
    def spawn2(self):
        if self.limit1:
            obj4 = Barbarian(8,16)
            obj4.add()
            self.troops.append(obj4)
            self.limit1 -= 1
    
    def spawn3(self):
        if self.limit1:
            obj4 = Barbarian(14,16)
            obj4.add()
            self.troops.append(obj4)
            self.limit1 -= 1

    def spawn4(self):
        if self.limit2:
            obj4 =  Archer(16,4)
            obj4.add()
            self.troops.append(obj4)
            self.limit2 -= 1
    
    def spawn5(self):
        if self.limit2:
            obj4 = Archer(24,4)
            obj4.add()
            self.troops.append(obj4)
            self.limit2 -= 1

    def spawn6(self):
        if self.limit2:
            obj4 = Archer(26,4)
            obj4.add()
            self.troops.append(obj4)
            self.limit2 -= 1
    
    def spawn7(self):
        if self.limit3:
            obj4 = Balloon(24,10)
            obj4.add()
            self.troops.append(obj4)
            self.limit3 -= 1
    
    def spawn8(self):
        if self.limit3:
            obj4 = Balloon(15,20)
            obj4.add()
            self.troops.append(obj4)
            self.limit3 -= 1
    
    def spawn9(self):
        if self.limit3:
            obj4 = Balloon(2,2)
            obj4.add()
            self.troops.append(obj4)
            self.limit3 -= 1

    def level2(self):
        for i in self.buildings:
            i.health = i.maxhlt
            i.update()

        obj = WizTower(16,50)
        obj.add()
        self.buildings.append(obj)
        self.defense.append(obj)

        obj = Cannon(16,30)
        obj.add()
        self.buildings.append(obj)
        self.defense.append(obj)

        self.limit1 = 6
        self.limit2 = 6
        self.limit3 = 3
    
    def level3(self):
        for i in self.buildings:
            i.health = i.maxhlt
            i.update()

        obj = WizTower(10,50)
        obj.add()
        self.buildings.append(obj)
        self.defense.append(obj)

        obj = Cannon(10,30)
        obj.add()
        self.buildings.append(obj)
        self.defense.append(obj)

        self.limit1 = 6
        self.limit2 = 6
        self.limit3 = 3
        