import item

class Player:
    def __init__(self):
        pass

    def getHealth(self):
        return self.health_

    def raiseHealth(self, heal):
        self.health_ += heal
    
    def lowerHealth(self, damage):
        self.health_ -= damage
    
    def showInv(self):
        print(*self.inventory_, sep = "\n")
    
    def searchInv(self, name):
        if name.lower().strip() in self.inventory_:
            return True

    def addInv(self, item):
        self.inventory_.append(item)

    def getCurrentRoom(self):
        return self.currentRoom_
    
    def setCurrentRoom(self, roomId):
        self.currentRoom_ = roomId

    def attack(self, item):
        return item.getItemDamage()
    
    
    
    health_ = 100
    inventory_ = []
    currentRoom_ = 0