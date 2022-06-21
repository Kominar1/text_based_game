from item import *

class Player:
    def __init__(self, name, currentRoom):
        self.name_ = name
        self.currentRoom_ = currentRoom
        self.inventory_ = []

    #Health functions
    def getHealth(self):
        return self.health_
    def raiseHealth(self, heal):
        self.health_ += heal
    def lowerHealth(self, damage):
        self.health_ -= damage    
    def setHealth(self, health):
        self.health_ = health

    #Inventory functions
    def showInv(self):
        i = 0
        if not self.inventory_:
            print("Your inventory is empty.")
        else:
            print("///////////////////////////////////////////////////////")
            for x in self.inventory_:
                print(self.inventory_[i].getName())
                i+=1
            print("///////////////////////////////////////////////////////")    
    def searchInv(self, item):
        if item in self.inventory_:
            return True
    def addInv(self, item):
        self.inventory_.append(item)

    #Room functions
    def getCurrentRoom(self):
        return self.currentRoom_   
    def setCurrentRoom(self, roomName):
        self.currentRoom_ = roomName

    #Equip functions
    def searchItem(self, item):
        i = 0
        for x in self.inventory_:
            if(self.inventory_[i].getName() == item):
                return self.inventory_[i]
            i+=1
    def equipItem(self, item):
        print(item)
        itemEquiped = self.searchItem(item)
        if(self.searchInv(itemEquiped)):
            self.equiped_ = itemEquiped
        else:
            print("You don't have this item in your inventory.")
    def checkEquiped(self):
        print("You have the " + self.equiped_.getName() + " equiped.")
    
    def attack(self, ):
        return self.equiped_.getItemDamage()    
    def checkIfDead(self):
        if self.health_ != 0:
            return False
        return True

    health_ = 100
    inventory_ = []
    currentRoom_ = ""
    name_ = ""
    equiped_ = Item("blank", 0)
