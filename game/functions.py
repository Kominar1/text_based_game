import time
import sys

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
    print("Exit: Leaves the game.")
    print("Load: Loads previous save.")
    print("Save: Saves current game.")
    print("Equip: Lets you equip an item from your inventory.")
    print("In Use: Lets you check which item you have equiped.")
    print("Attack: Lets you attack an enemy by typing attack and then the name of the enemy.")
    print("Enemies: Gives you a list of enemies you can attack.")
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
            delay_print("You are already in this room.\n") 
            choice = input()
            getChoice(choice, player, rooms)

        if current.getTheRight() in choice:
            player.setCurrentRoom(current.getTheRight())

        if current.getTheLeft() in choice:
            player.setCurrentRoom(current.getTheLeft())

        if current.getAhead() in choice:
            player.setCurrentRoom(current.getAhead())

        if current.getBehind() in choice:
            player.setCurrentRoom(current.getBehind())
    #Done
    if "look" in choice:
        print(current.getLook())
    #Done
    if "available" in choice:
        if(current.getTheRight() != "null"):
            print(current.getTheRight())

        if(current.getTheLeft() != "null"):
            print(current.getTheLeft())

        if(current.getAhead() != "null"):
            print(current.getAhead())

        if(current.getBehind() != "null"):
            print(current.getBehind())
        choice = input()
        getChoice(choice, player, rooms)
    #Done
    if "current" in choice:
        print("You are currently in the " + player.getCurrentRoom() + ".")
    #Done
    if "exit" in choice:
        sys.exit()
    #Done
    if "start" in choice:
        return True
    #
    if "grab" in choice:
        item = ""
        i = 0
        for x in current.contents_:
            if current.contents_[i].getName() in choice:
                item = current.contents_[i].getName()
            i+=1
        if(current.searchContents(item)):
            player.addInv(searchItems(current, item))
            current.removeContents(searchItems(current, item))
        print("You have successfully added " + item + " to your inventory!")
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
        f.write(player.equiped_.getName() + "\n")
        f.close()
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
        player.equipItem(lines[lineLength][:-1])
        return True
    #Done
    if "equip" in choice:
        for i in range(len(player.inventory_)):
            if player.inventory_[i].getName() in choice:
                item = player.inventory_[i].getName()
        if item in choice:
            player.equipItem(item)
    #Done
    if "in use" in choice:
        player.checkEquiped()
    
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
            block = False
            while(player.checkIfDead() == False and enemy.checkIfDead() == False and flee == False):
                block = False
                #Do you want to attack block or flee
                print("Would you like to attack, block or flee?")
                choice = input()
                if(choice.strip().lower() == "attack"):
                    enemy.lowerHealth(player.attack())
                elif(choice.strip().lower() == "block"):
                    block = player.block()                
                elif(choice.strip().lower() == "flee"):
                    flee = True

                if(block == False):
                    player.lowerHealth(enemy.attack())
    #Done
    if "enemies" in choice:
        current.getEnemies()

    if "heal" in choice:
        if choice == "heal":
            player.heal()
def searchRooms(roomsIndex, room):
    for i in range(len(roomsIndex)):
        if (roomsIndex[i].getName() == room):
            this = roomsIndex[i]
            return this

def searchItems(room, item):
    for i in range(len(room.contents_)):
        if (room.contents_[i].getName() == item):
            this = room.contents_[i]
            return this

def getItem(player, rooms, item):
    current = searchRooms(rooms, player.getCurrentRoom())
    currentItem = searchItems(current, item)
    if current.searchContents(currentItem):
        current.removeContents(currentItem)
        player.addInv(currentItem)