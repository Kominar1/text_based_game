import time
import sys
from item import *

#Windows path: e:/Projects/text_game/game/save.txt
#Linux path: /home/kominar/Visual Studio/Projects/text_game/game/save.txt

def delay_print(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.03)

def printHelp():
    print("Help: Brings you to this menu.")
    print("Health: Shows your current health count.")
    print("Inventory: Shows the items in your inventory.")
    print("Items: Prints a list of available items in the room.")
    print("Grab: Type grab and then the item you want to get.")
    print("Move: Type move and the room you want to move to.")
    print("Look: Tells you some aditional information about the space.")
    print("Available: List of rooms available to move to.")
    print("Current: Tells the name of the current room you are in.")
    print("Save: Saves current game.")
    print("Load: Loads previous save.")
    print("Equip: Let's you equip a weapon from your inventory.")
    print("Put on: Let's you put on a piece of armor.")
    print("In Use: Let's you check which item you have equiped.")
    print("Check: Let's you check the amount of damage or healing or protection an item gives you.")
    print("Attack: Let's you attack an enemy by typing attack and then the name of the enemy.")
    print("Enemies: Gives you a list of enemies you can attack.")
    print("Exit: Leaves the game.")
    print("Start: Starts the game.")

def getChoice(choice, player, rooms, items):
    current = searchRooms(rooms, player.getCurrentRoom())
    choice = choice.strip().lower()
    item = ""
    #Done
    if "help" in choice:
        printHelp()
    #Done
    if "health" in choice:
        if choice == "health":
            print("Your health is at: " + str(player.getHealth()))
    #Done
    if "inventory" in choice:
        player.showInv()
    #Done
    if "items" in choice:
        current.getContents()
    #Done
    if "move" in choice:
        #Get the room from the string
        if player.getCurrentRoom() in choice:
            print("You are already in this room.\n") 

        if current.getTheRight() in choice:
            player.setCurrentRoom(current.getTheRight())
        elif current.getTheLeft() in choice:
            player.setCurrentRoom(current.getTheLeft())
        elif current.getAhead() in choice:
            player.setCurrentRoom(current.getAhead())
        elif current.getBehind() in choice:
            player.setCurrentRoom(current.getBehind())
        else:
            print("There is no room by that name available.")
    #Done
    if "look" in choice:
        print(current.getLook())
    #Done
    if "available" in choice:
        print("Rooms that you can move to are: ")
        if(current.getTheRight() != "null"):
            print(current.getTheRight())

        if(current.getTheLeft() != "null"):
            print(current.getTheLeft())

        if(current.getAhead() != "null"):
            print(current.getAhead())

        if(current.getBehind() != "null"):
            print(current.getBehind())
    #Done
    if "current" in choice:
        print("You are currently in the " + player.getCurrentRoom() + ".")
    #Done
    if "exit" in choice:
        sys.exit()
    #Done
    if "start" in choice:
        return True
    #Done
    if "grab" in choice:
        item = getItemInRoom(current, choice)
        if isinstance(item, Weapon) or isinstance(item, Armor) or isinstance(item, HealthStim):
            if player.searchInv(item):
                print("You already have this item in your inventory.")
            elif current.searchContents(item.getName()):
                player.addInv(item)
                current.removeContents(item)
                print("You have successfully added " + item.getName() + " to your inventory!")
        else:
            print("There is no item here by that name.")
    #Done
    if "save" in choice:
        f = open("e:/Projects/text_game/game/save.txt", "w")
        i = 0
        length = len(player.inventory_)
        f.write(str(length) + "\n")
        for x in player.inventory_:
            f.write(player.inventory_[i].getName() + "\n")
            i+=1
        f.write(str(player.getHealth()) + "\n")
        f.write(player.getCurrentRoom() + "\n")
        f.write(player.name_ + "\n")
        f.write(player.weapon_.getName() + "\n")
        f.write(player.armor_.getName() + "\n")
        f.close()
        print("You successfully saved the game!")
    #Done
    if "load" in choice:
        f = open("e:/Projects/text_game/game/save.txt")
        lines = f.readlines()
        f.close()
        lineLength = int(lines[0])
        itemsLength = len(items)
        i=1
        while(i <= lineLength):
            j = 0
            while(j<itemsLength):
                if(items[j].getName() == lines[i].strip().lower()):
                    player.addInv(items[j])
                    break
                else:
                    j+=1
            i+=1
        lineLength+=1
        #get the sting and delete the \n from it
        player.setHealth = int(lines[lineLength][:-1])
        lineLength+=1
        player.setCurrentRoom(lines[lineLength][:-1])
        lineLength+=1
        player.setName(lines[lineLength][:-1])
        lineLength+=1
        if lines[lineLength][:-1] != "blank":
            player.equipItem(lines[lineLength][:-1])
        lineLength+=1
        if lines[lineLength][:-1] != "blank":
            player.putOnArmor(lines[lineLength][:-1])
        return True
    #Done
    if "equip" in choice:
        item = getItemInInventory(player, choice)
        if item.getName() in choice:
            player.equipItem(item)
    #Done
    if "in use" in choice:
        player.checkEquiped()
    #need to rework
    if "attack" in choice:
        enemyName = ""
        for i in range(len(current.enemies_)):
            if current.enemies_[i].getName() in choice:
                enemyName = current.enemies_[i].getName()
        if(current.searchEnemies(enemyName) == False):
            print("There is nothing here with that name.")
        else:
            enemy = current.searchEnemies(enemyName)
            flee = False
            while(player.checkIfDead() == False and enemy.checkIfDead() == False and flee == False):
                block = False
                #Do you want to attack block or flee
                print("Would you like to attack, block or flee?")
                choice = input()
                if "attack" in choice:
                    enemy.lowerHealth(player.attack())
                elif "block" in choice:
                    block = player.block()                
                elif "flee" in choice:
                    flee = True

                if(block == False):
                    player.lowerHealth(enemy.attack())
    #Done
    if "enemies" in choice:
        print("Current enemies in the room are: ")
        current.getEnemies()
    #Done
    if "heal" in choice:
        if choice == "heal":
            player.heal()
    #Done
    if "check" in choice:
        item = getItemInInventory(player, choice)
        if item.getName() == '':
            print("This item is not in your inventory.")
        else:
            item.check()

    if "put on" in choice:
        item = getItemInInventory(player, choice)
        player.putOnArmor(item)

def searchRooms(roomsIndex, room):
    for i in range(len(roomsIndex)):
        if (roomsIndex[i].getName() == room):
            return roomsIndex[i]

def getItemInRoom(room, choice):
    for i in range(len(room.contents_)):
        if room.contents_[i].getName() in choice:
            return room.contents_[i]

def getItemInInventory(player, choice):
   for i in range(len(player.inventory_)):
        if player.inventory_[i].getName() in choice:
            return player.inventory_[i]
            