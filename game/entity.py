from item import *
import random

class Entity:
    def __init__(self, name, currentRoom):
        self.name_ = name
        self.currentRoom_ = currentRoom
        self.health_ = 100
    #Health functions
    def getHealth(self):
        return self.health_
    def raiseHealth(self, heal):
        self.health_ += heal
    def lowerHealth(self, damage):
        self.health_ -= damage    
    def setHealth(self, health):
        self.health_ = health

    def checkIfDead(self):
        if self.health_ != 0:
            return False
        return True

class Player(Entity):
    def __init__(self, name, currentRoom):
        super().__init__(name, currentRoom)
        self.inventory_ = []
        self.equiped_ = Item("blank", 0)

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
    def setName(self, name):
        self.name_ = name

class Enemy(Entity):
    def __init__(self, name, currentRoom, attack, dodgeChance):
        super().__init__(name, currentRoom)
        self.attack_ = attack
        self.dodgeChance_ = dodgeChance

    def attack(self):
        return self.attack_

    def dodgeChance(self):
        return random.randrange(1, self.dodgeChance_, 1)

    def getName(self):
        return self.name_

    def lowerHealth(self, damage):
        if(self.dodgeChance() != 2):
            self.health_ -= damage
            print("You hit them! They have " + str(self.getHealth()) + " health left!")
        else:
            print("Oh no! They dodged away from your attack! You did no damage!")