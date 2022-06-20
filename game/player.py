import item

class Player:
    def __init__(self, name, currentRoom):
        self.name_ = name
        self.currentRoom_ = currentRoom
        self.inventory_ = []

    def setName(self, name):
        self.name_ = name

    def getHealth(self):
        return self.health_

    def raiseHealth(self, heal):
        self.health_ += heal
    
    def lowerHealth(self, damage):
        self.health_ -= damage
    
    def setHealth(self, health):
        self.health_ = health

    def showInv(self):
        i = 0
        for x in self.inventory_:
            print(self.inventory_[i].getName())
            i+=1
    
    def searchInv(self, item):
        if item in self.inventory_:
            return True

    def addInv(self, item):
        self.inventory_.append(item)

    def getCurrentRoom(self):
        return self.currentRoom_
    
    def setCurrentRoom(self, roomName):
        self.currentRoom_ = roomName

    def attack(self, item):
        return item.getItemDamage()
    
    def checkIfDead(self):
        if self.health_ != 0:
            return False
        return True
    
    health_ = 100
    inventory_ = []
    currentRoom_ = ""
    name_ = ""
