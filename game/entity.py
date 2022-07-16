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
        if(self.getHealth() <= 0):
            return True
        else:
            return False

class Player(Entity):
    def __init__(self, name, currentRoom):
        super().__init__(name, currentRoom)
        self.inventory_ = []
        self.equiped_ = Weapon("blank", 1)

    def lowerHealth(self, damage):
        self.health_ -= damage
        print("You've been hit! Your health is now at " + str(self.getHealth()) + ".")
    
    #Inventory functions
    def showInv(self):
        if not self.inventory_:
            print("Your inventory is empty.")
        else:
            print("///////////////////////////////////////////////////////")
            for i in range(len(self.inventory_)):
                print(self.inventory_[i].getName())
            print("///////////////////////////////////////////////////////")    
    def searchInv(self, item):
        if item in self.inventory_:
            return True
    def addInv(self, item):
        self.inventory_.append(item)
    def removeInv(self, item):
        self.inventory_.remove(item)

    #Room functions
    def getCurrentRoom(self):
        return self.currentRoom_   
    def setCurrentRoom(self, roomName):
        self.currentRoom_ = roomName

    #Equip functions
    def searchItem(self, item):
        for i in range(len(self.inventory_)):
            if(self.inventory_[i].getName() == item):
                return self.inventory_[i]
    def equipItem(self, item):
        print(item)
        itemEquiped = self.searchItem(item)
        if(self.searchInv(itemEquiped)):
            self.equiped_ = itemEquiped
            print("You equiped the " + self.equiped_.getName())
        else:
            print("You don't have this item in your inventory.")
    
    def checkEquiped(self):
        print("You have the " + self.equiped_.getName() + " equiped.")
    
    def attack(self):
        return self.equiped_.getItemDamage()    
    def block(self):
        print("You blocked the attack!")
        return True
    def setName(self, name):
        self.name_ = name
    def heal(self):
        healthStim = self.searchItem("health stim")
        if self.searchInv(healthStim):
            if self.getHealth() == 100:
                print("You are already at full health!")
            else:
                self.raiseHealth(healthStim.getHealing())
                if self.getHealth() > 100:
                    self.health_ = 100
                self.removeInv(healthStim)
                print("You used a health stim! Health now at " + str(self.getHealth()) + ".\n")
        else:
            print("You don't have any health stims in your inventory.\n")

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
        if(self.checkIfDead()):
            print("You killed it!")
        else:
            if(self.dodgeChance() != 2):
                self.health_ -= damage
                print("You hit them! They have " + str(self.getHealth()) + " health left!")
            else:
                print("Oh no! They dodged away from your attack! You did no damage!")