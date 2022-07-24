class Item:
    def __init__(self, name, attribute, itemNum):
        self.name_= name
        self.attribute_ = attribute
        self.itemNum_ = itemNum

    def getName(self):
        return self.name_

    def getAttribute(self):
        return self.attribute_

    def check(self):
        print("The " + self.getName() + " doesn't seem to have a purpose yet.")
    
    def getNum(self):
        return self.itemNum_

class Weapon(Item):
    def check(self):
        print("This weapon does " + str(self.getAttribute()) + " damage.")
    
class HealthStim(Item):
    def check(self):
        print("This health stim restores " + str(self.getAttribute()) + " hp.")

class Armor(Item):
    def check(self):
        print("Your armor takes away " + str(self.getAttribute() * 100) + "% of the damage taken.")
