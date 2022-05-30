// Python Game //

Initially a village is generated with pre-defined buildings

Now, King has to attack the village along with his troops(barbarians) which are generated
from pre-defined spawning points

Goal is to destroy the village

Special spells can be used to destroy the village

If you destroy all non-wall buildings in the village you win 

All buildings health is displayed by their color (RED - health < 20% , YELLOW - 20% <= health <= 50%, GREEN - health > 50%)

If King and his troops are destoyed before the vilage you lose

King:
    King controls: W(up),A(left),S(down),D(right),SPACE(attack)
    King starts at (0,0)
    King health bar is displayed at top of the village grid
    King max health is 100
    King can damage 5 with a single hit
    Represented by "K>" in MAGNETA color
    King's leviathan axe can be activated with "X", it attacks every building in its 5 tile radius

Barbarian:
    Barbarian spawning keys: C,V,B
    Barbarian moves to the closest non-wall building (implemented using Euclidean distance)
    Barbarian max health is 40
    Barbarian can damage 5 with a single hit
    Represented by "B" in MAGNETA color

Cannons:
    Vilage is defended by cannons
    They hit troops or king when in the range and can only hit one object at a time
    They can damage 5 with one hit 
    Cannon range is 6
    Cannon health is 50
    Represented by "C" as a building(1x3)

TownHall:
    Health is 200
    Dimensions - (4x3)

Wall:
    Health is 30
    Dimensions - (1x1)

Hut:
    Heatlh is 50
    Dimensions - (2x2)
 
Cannon destructor spell:
	Can be used only once in a game
	Decreases cannon health to its half



Inheritance,Polymorphism,Encapsulation,Abstraction were used to program this game along with colorama and other libraries

New extensions to the game:

We can choose a king or queen at the beginning of the game

3 Levels are introduced (You win a level and move to the next level)

Troops are constrained by limits which reset every level

Limits for troops:
Barbarians - 6
Archers - 6
Balloons - 3

Queen:
    Same controls as king
    Attack is different from king, attacks 5x5 area whose centre is 8 tiles away
    Damage is less than king 

Balloon:
    Can pass through walls and buildings
    Focuses on destroying defensive buildings
    Spawning keys: I,O,P

Archer:
    Same as barbarian but can attack over the wall and attack has a range(range is > cannon's range)
    Spawning keys: J,K,L


Wizard Tower:
    Same as cannon but can attack balloons and attacks 3x3 area around the target



