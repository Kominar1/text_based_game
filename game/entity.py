from item import *
import random

class Entity:
    def __init__(self, name, currentRoom):
        self.name_ = name
        self.currentRoom_ = currentRoom
        self.health_ = 100

    #Health functions
    def getHealth(self):
        return str(self.health_)
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
        self.weapon_ = Weapon("blank", 1, 0)
        self.armor_ = Armor("blank", 0, 0)

    def lowerHealth(self, damage):
        if self.armor_.getName != "Blank":
            blocked = damage * self.armor_.getAttribute()
            damage -= blocked
            self.health_ -= damage
        print("You've been hit! Your health is now at " + str(self.getHealth()) + ".")
    
    #Inventory functions
    def showInv(self):
        if not self.inventory_:
            return "Your inventory is empty."
        else:
            string = ""
            for i in range(len(self.inventory_)):
                string = string + (self.inventory_[i].getName() + '\n')
            return string
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
        itemEquiped = self.searchItem(item)
        if isinstance(itemEquiped, Weapon):
            if self.searchInv(itemEquiped):
                self.weapon_ = itemEquiped
                return "You equiped the " + self.weapon_.getName() + "!"
            else:
                return"You don't have this item in your inventory."
        else:
            if(self.searchInv(item)):
                self.weapon_ = item
                return "You equiped the " + self.weapon_.getName() + "!"
            else:
                return "You don't have this item in your inventory."
    def checkEquiped(self):
        string = ""
        if self.weapon_.getName() == "blank":
            string = "You don't have any weapon equiped right now.\n"
        else:
            string = "You have the " + self.weapon_.getName() + " equiped.\n"
        if self.armor_.getName() == "blank":
            string = string + "You don't have any armor on right now."
        else:
            string = string + "You have the " + self.armor_.getName() + " on."
        return string
    def putOnArmor(self, armor):
        armorEquiped = self.searchItem(armor)
        if isinstance(armorEquiped, Armor):
            if self.searchInv(armorEquiped):
                self.armor_ = armorEquiped
                return "You put the " + self.armor_.getName() + " on!"
            else:
                return "You don't have this in your inventory."
        else:
            if self.searchInv(armor):
                self.armor_ = armor
                return "You put the " + self.armor_.getName() + " on!"
            else:
                return "You don't have this in your inventory."

    def attack(self):
        return self.weapon_.getAttribute()    
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
                if self.getAttribute() > 100:
                    self.health_ = 100
                self.removeInv(healthStim)
                print("You used a health stim! Health now at " + str(self.getAttribute()) + ".\n")
        else:
            print("You don't have any health stims in your inventory.\n")

class Enemy(Entity):
    def __init__(self, name, currentRoom, attack, dodgeChance):
        super().__init__(name, currentRoom)
        self.attack_ = attack
        self.dodgeChance_ = dodgeChance

    #add a chance for an attack that does damage and a half
    def attack(self):
        if self.dodgeChance() == 2:
            return self.attack_ * 2
        else:
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