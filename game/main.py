from functions import *
from entity import *
from item import *
from room import *

printHelp()
choice = input()
choice = choice.strip().lower()

#Creating player
player = Player("Player", "basement")

#Creating rooms
basement = Room("basement", 1, "null", "null", "corridor", "null")
corridor = Room("corridor", 2, "null", "bedroom", "hallway", "basement")
bedroom = Room("bedroom", 3, "corridor", "null", "null", "null")
hallway = Room("hallway", 4, "cell", "null", "null", "corridor")
cell = Room("cell", 5, "null", "null", "null", "hallway")
rooms = [basement, corridor, bedroom, hallway, cell]

#Creating items
flashlight = Weapon("flashlight", 5, 1)
knife = Weapon("knife", 12, 1)
bat = Weapon("bat", 15, 1)
gun = Weapon("gun", 30, 1)
healthStim = HealthStim("health stim", 30, 2)
helmet = Armor("helmet", 0.1, 2)
items = [flashlight, knife, bat, gun, healthStim, helmet]

#Creating enemy
entity = Enemy("distorted", "cell", 10, 100)

#Adding objects to rooms
basement.addContents(flashlight)
corridor.addContents(bat)
corridor.addContents(helmet)
bedroom.addContents(knife)
cell.addContents(gun)
cell.addContents(healthStim)
cell.addEnemy(entity)

dead = False
first = True
    
if getChoice(choice, player, rooms, items):
    while(dead != True):
        currentRoom = searchRooms(rooms, player.getCurrentRoom())
        if(first == True):
            currentRoom.getDiscription()
            first = False
        choice = input()
        if "move" in choice:
            first = True
        if "load" in choice:
            first = True
        getChoice(choice, player, rooms, items)
    if dead:
        print("You died!")
