class Item:
    def __init__(self, name):
        self.name_= name

    def getName(self):
        return self.name_

class Weapon(Item):
    def __init__(self, name, damage):
        super().__init__(name)
        self.damage_ = damage

    def getItemDamage(self):
        return self.damage_

class HealthStim(Item):
    def __init__(self, name, healing):
        super().__init__(name)
        self.healing_ = healing

    def getHealing(self):
        return self.healing_