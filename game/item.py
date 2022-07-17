class Item:
    def __init__(self, name, attribute):
        self.name_= name
        self.attribute_ = attribute

    def getName(self):
        return self.name_

    def getAttribute(self):
        return self.attribute_

    def check(self):
        pass

class Weapon(Item):
    def check(self):
        print("This weapon does " + str(self.getAttribute()) + " damage.")
    
class HealthStim(Item):
    def check(self):
        print("This health stim restores " + str(self.getAttribute()) + " hp.")

class Armor(Item):
    def check(self):
        print("Your armor takes away " + str(self.getAttribute() * 100) + "% of the damage taken.")
