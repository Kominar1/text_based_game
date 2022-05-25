from os import abort
import time
import sys
from player import *
from item import *
from room import *


def delay_print(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.03)

def printHelp():
    delay_print("Help: Brings you to this menu.\n")
    delay_print("Health: Shows your current health count.\n")
    delay_print("Inventory: Shows the items in your inventory.\n")
    delay_print("Move: Type move and the room you want to move to.\n")
    delay_print("Available: List of rooms available to move to.\n")
    delay_print("Current: Tells the name of the current room you are in.\n")
    delay_print("Exit: Leaves the game.\n")
    delay_print("Load: Loads previous save.\n")
    delay_print("Save: Saves current game.\n")
    delay_print("Start: Starts the game.\n")

def getChoice(choice, player):
    if (choice.strip().lower() == "help"):
        printHelp()
    if(choice.strip().lower() == "health"):
        delay_print(player.getHealth())
    if(choice.strip().lower() == "inventory"):
        player.showInv()
    if(choice.strip().lower() == "move"):
        room = input()
        if(room.strip().lower() == player.getCurrentRoom()):
            delay_print("You are already in this room.\n") 
        if(room.strip().lower() == player.getTheRight()):
            player.setCurrentRoom(room)
        if(room.strip().lower() == player.getTheLeft()):
            player.setCurrentRoom(room)
        if(room.strip().lower() == player.getAhead()):
            player.setCurrentRoom(room)
        if(room.strip().lower() == player.getBehind()):
            player.setCurrentRoom(room)
    if(choice.strip().lower() == "available"):
        if(player.getTheRight() != "null"):
            delay_print(player.getTheRight())
        if(player.getTheLeft() != "null"):
            delay_print(player.getTheLeft())
        if(player.getAhead() != "null"):
            delay_print(player.getAhead())
        if(player.getBehind() != "null"):
            delay_print(player.getBehind())
    if(choice.strip().lower() == "current"):
        delay_print(player.getCurrentRoom())
    if(choice.strip().lower() == "exit"):
        abort
    if(choice.strip().lower() == "start"):
        return True
    


player = Player("Kominar", "basement")
basement = Room("basement", 1, "null", "null", "hallway", "null")
hallway = Room("hallway", 2, "null", "bedroom", "hallway2", "basement")
bedroom = Room("bedroom", 3, "hallway", "null", "null", "null")
hallway2 = Room("hallway2", 4, "cells", "null", "warproom", "hallway")
cell = Room("cell", 5, "hallway2", "null", "null", "null")
flashlight = Item("flashlight", 5)
knife = Item("knife", 12)
bat = Item("baseballbat", 15)
gun = Item("gun", 30)
basement.addContents(flashlight)
hallway.addContents(bat)
bedroom.addContents(flashlight)
bedroom.addContents(knife)
cell.addContents(gun)

printHelp()
choice = input()
start = False
dead = False
getChoice(choice, player)

if start:
    while(dead != True):
        basement.getDiscription()
