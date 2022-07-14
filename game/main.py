from functions import *
from entity import *
from item import *
from room import *

printHelp()
choice = input()
choice = choice.strip().lower()

#Creating objects
player = Player("Player", "basement")
basement = Room("basement", 1, "null", "null", "corridor", "null")
corridor = Room("corridor", 2, "null", "bedroom", "hallway", "basement")
bedroom = Room("bedroom", 3, "corridor", "null", "null", "null")
hallway = Room("hallway", 4, "cell", "null", "warproom", "hallway")
cell = Room("cell", 5, "hallway2", "null", "null", "null")
rooms = [basement, corridor, bedroom, hallway, cell]
flashlight = Item("flashlight", 5)
knife = Item("knife", 12)
bat = Item("bat", 15)
gun = Item("gun", 30)
items = [flashlight, knife, bat, gun]
entity = Enemy("distorted", "cell", 10, 100)

#Adding objects to rooms
basement.addContents(flashlight)
corridor.addContents(bat)
bedroom.addContents(flashlight)
bedroom.addContents(knife)
cell.addContents(gun)
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
        if(choice[0:4].strip().lower() == "move"):
            first = True
        getChoice(choice, player, rooms, items)
