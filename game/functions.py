import time
import sys
from item import *
from room import *

#Windows path: e:/Projects/text_game/game/save.txt
#Linux path: /home/kominar/Visual Studio/Projects/text_game/game/save.txt

def delay_print(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.03)

def makeMap(mapOrItem):
    basement = Room("basement", 1, "null", "null", "corridor", "null")
    corridor = Room("corridor", 2, "null", "bedroom", "hallway", "basement")
    bedroom = Room("bedroom", 3, "corridor", "null", "null", "null")
    hallway = Room("hallway", 4, "cell", "null", "stairs", "corridor")
    cell = Room("cell", 5, "null", "null", "null", "hallway")
    stairs = Room("stairs", 6, "null", "null", "entrence", "hallway")
    entrance = Room("entrance", 7, "machine room", "control room", "null", "stairs")
    machineRoom = Room("machine room", 8, "null", "null", "null", "entrance")
    
    flashlight = Weapon("flashlight", 5, 1)
    knife = Weapon("knife", 12, 1)
    bat = Weapon("bat", 15, 1)
    gun = Weapon("gun", 30, 1)
    healthStim = HealthStim("health stim", 30, 2)
    helmet = Armor("helmet", 0.1, 2)
    sword = Weapon("sword", 35, 1)
    strangeDevice = Item("strange device", "none", 1)

    entity = Enemy("distorted", "cell", 10, 100)

    basement.addContents(flashlight)
    corridor.addContents(bat)
    corridor.addContents(helmet)
    bedroom.addContents(knife)
    cell.addContents(gun)
    cell.addContents(healthStim)
    cell.addEnemy(entity)
    entrance.addContents(sword)
    machineRoom.addContents(strangeDevice)

    if mapOrItem == "map":
        return [basement, corridor, bedroom, hallway, cell, stairs, entrance, machineRoom]
    elif mapOrItem == "item":
        return [flashlight, knife, bat, gun, healthStim, helmet, sword,strangeDevice]

def printHelp():
    return """Help: Brings you to this menu.
Health: Shows your current health count.
Inventory: Shows the items in your inventory.
Items: Prints a list of available items in the room.
Grab: Type grab and then the item you want to get.
Move: Type move and the room you want to move to.
Look: Tells you some aditional information about the space.
Available: List of rooms available to move to.
Current: Tells the name of the current room you are in.
Save: Saves current game.
Load: Loads previous save.
Equip: Let's you equip a weapon from your inventory.
Put on: Let's you put on a piece of armor.
In Use: Let's you check which item you have equiped.
Check: Let's you check the amount of damage or healing or protection an item gives you.
Attack: Let's you attack an enemy by typing attack and then the name of the enemy.
Enemies: Gives you a list of enemies you can attack.
Exit: Leaves the game.
Start: Starts the game."""

def save(player):
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

def load(items, player):
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

def getChoice(choice, player, rooms, items):
    current = searchRooms(rooms, player.getCurrentRoom())
    choice = choice.strip().lower()
    item = ""
    #Done
    if "help" in choice:
        return printHelp()
    #Done
    if "health" in choice:
        if choice == "health":
            return "Your health is at: " + str(player.getHealth())
    
    if "inventory" in choice:
        return player.showInv()
    
    if "items" in choice:
        current.getContents()
    #Done
    if "move" in choice:
        #Get the room from the string
        if player.getCurrentRoom() in choice:
            return "You are already in this room.\n"

        if current.getTheRight() in choice:
            player.setCurrentRoom(current.getTheRight())
        elif current.getTheLeft() in choice:
            player.setCurrentRoom(current.getTheLeft())
        elif current.getAhead() in choice:
            player.setCurrentRoom(current.getAhead())
        elif current.getBehind() in choice:
            player.setCurrentRoom(current.getBehind())
        else:
            return "There is no room by that name available."
    
    if "look" in choice:
        return current.getLook()
    
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
        return "You are currently in the " + player.getCurrentRoom() + "."
    #Done
    if "exit" in choice:
        sys.exit()
    #Done
    if "grab" in choice:
        item = getItemInRoom(current, choice)
        if isinstance(item, Weapon) or isinstance(item, Armor) or isinstance(item, HealthStim):
            if player.searchInv(item):
                return "You already have this item in your inventory."
            elif current.searchContents(item.getName()):
                player.addInv(item)
                current.removeContents(item)
                return "You have successfully added " + item.getName() + " to your inventory!"
        else:
            return "There is no item here by that name."
    
    if "equip" in choice:
        item = getItemInInventory(player, choice)
        if item.getName() in choice:
            player.equipItem(item)

    if "in use" in choice:
        return player.checkEquiped()
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
    
    if "enemies" in choice:
        print("Current enemies in the room are: ")
        current.getEnemies()
    
    if "heal" in choice:
        if choice == "heal":
            player.heal()
    #Done
    if "check" in choice:
        item = getItemInInventory(player, choice)
        if item.getName() == '':
            return "This item is not in your inventory."
        else:
            return item.check()

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
