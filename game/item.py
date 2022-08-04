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
        return "The " + self.getName() + " doesn't seem to have a purpose yet."
    
    def getNum(self):
        return self.itemNum_

class Weapon(Item):
    def check(self):
        return "This weapon does " + str(self.getAttribute()) + " damage."
    
class HealthStim(Item):
    def check(self):
        return "This health stim restores " + str(self.getAttribute()) + " hp."

class Armor(Item):
    def check(self):
        damageSaved = self.attribute_ * 100
        return "Your armor takes away " + str(damageSaved) + "% of the damage taken."
