from functions import *
from player import *
from item import *
from room import *

printHelp()
choice = input()
player = Player("Player", "basement")
basement = Room("basement", 1, "null", "null", "hallway", "null")
hallway = Room("hallway", 2, "null", "bedroom", "hallway2", "basement")
bedroom = Room("bedroom", 3, "hallway", "null", "null", "null")
hallway2 = Room("hallway2", 4, "cells", "null", "warproom", "hallway")
cell = Room("cell", 5, "hallway2", "null", "null", "null")
rooms = [basement, hallway, bedroom, hallway2, cell]
flashlight = Item("flashlight", 5)
knife = Item("knife", 12)
bat = Item("bat", 15)
gun = Item("gun", 30)
basement.addContents(flashlight)
hallway.addContents(bat)
bedroom.addContents(flashlight)
bedroom.addContents(knife)
cell.addContents(gun)
dead = False
first = True
if(choice.strip().lower() == "load"):
    lines = getChoice(choice, player, rooms)
    player.setHealth(lines[0])
    
if getChoice(choice, player, rooms):
    while(dead != True):
        currentRoom = searchRooms(rooms, player.getCurrentRoom())
        if(first == True):
            currentRoom.getDiscription()
            first = False
        choice = input()
        if(choice.strip().lower() == "move"):
            first = True
        getChoice(choice, player, rooms)
