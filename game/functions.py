import time
import sys

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
    print("Start: Starts the game.")

def getChoice(choice, player, rooms):
    current = searchRooms(rooms, player.getCurrentRoom())
    #Check if the first part of the string is move or grab
    part = choice[0:4]
    part2 = choice[0:5]
    #Done
    if(choice.strip().lower() == "help"):
        printHelp()
    #Done
    if(choice.strip().lower() == "health"):
        print("Your health is at: " + player.getHealth())
    #Done
    if(choice.strip().lower() == "inventory"):
        player.showInv()
    #Done
    if(choice.strip().lower() == "items"):
        current.getContents()
    #Done
    if(part.strip().lower() == "move"):
        #Get the room from the string
        room = choice[5:]
        if(room.strip().lower() == player.getCurrentRoom()):
            delay_print("You are already in this room.\n") 
            choice = input()
            getChoice(choice, player, rooms)

        if(room.strip().lower() == current.getTheRight()):
            player.setCurrentRoom(room)

        if(room.strip().lower() == current.getTheLeft()):
            player.setCurrentRoom(room)

        if(room.strip().lower() == current.getAhead()):
            player.setCurrentRoom(room)

        if(room.strip().lower() == current.getBehind()):
            player.setCurrentRoom(room)
    #Almost done
    if(choice.strip().lower() == "look"):
        print(current.getLook())
        choice = input()
        getChoice(choice, player, rooms)
    #Done
    if(choice.strip().lower() == "available"):
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
    if(choice.strip().lower() == "current"):
        print("You are currently in the " + player.getCurrentRoom() + ".")
    #Done
    if(choice.strip().lower() == "exit"):
        sys.exit()
    #Done
    if(choice.strip().lower() == "start"):
        return True
    #Done
    if(part.strip().lower() == "grab"):
        item = choice[5:]
        if(current.searchContents(item)):
            player.addInv(searchItems(current, item))
            current.removeContents(searchItems(current, item))
        print("You have successfully added " + item + " to your invnetory!")
    #Done
    if(choice.strip().lower() == "save"):
        f = open("e:/Projects/text_game/game/save.txt", "w")
        i = 0
        length = len(player.inventory_)
        f.write(str(length) + "\n")
        for x in player.inventory_:
            f.write(player.inventory_[i].getName() + "\n")
            i+=1
        f.write(str(player.getHealth()) + "\n")
        f.write(player.getCurrentRoom() + "\n")
        f.write(player.name_)
        f.close()
    #Done
    if(choice.strip().lower() == "load"):
        f = open("e:/Projects/text_game/game/save.txt")
        lines = f.readlines()
        f.close()
        return lines

    if(part2.strip().lower() == "equip"):
        item = choice[6:]
        player.equipItem(item)
        print("You equiped the " + item)
    
    if(choice.strip().lower() == "in use"):
        player.checkEquiped()

def searchRooms(roomsIndex, room):
    i = 0
    for x in roomsIndex:
        if (roomsIndex[i].getName() == room):
            this = roomsIndex[i]
            return this
        i+=1

def searchItems(room, item):
    i = 0
    for x in room.contents_:
        if (room.contents_[i].getName() == item):
            this = room.contents_[i]
            return this
        i+=1

def getItem(player, rooms, item):
    current = searchRooms(rooms, player.getCurrentRoom())
    currentItem = searchItems(current, item)
    if current.searchContents(currentItem):
        current.removeContents(currentItem)
        player.addInv(currentItem)