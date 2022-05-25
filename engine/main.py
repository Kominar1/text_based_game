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

def getChoice():
    choice = input()
    if (choice.strip().lower() == "help"):
        printHelp()

player = Player("Kominar", "basement")
basement = Room("basement", 1, "null", "null", "hallway", "null")
flashlight = Item("flashlight", 5)
basement.addContents(flashlight)
getChoice()