class Item:
    def __init__(self, itemName, itemDamage):
        self.itemName_ = itemName
        self.itemDamage_ = itemDamage

    def getItemDamage(self):
        return self.itemDamage_

    def getName(self):
        return self.itemName_

    itemName_ = ""
    itemDamage_ = 0