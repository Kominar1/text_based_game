import random
class Enemy:
    def __init__(self, attack, dodgeChance, name):
        self.attack_ = attack
        self.dodgeChance_ = dodgeChance
        self.name_ = name

    def takeDamage(self, damage):
        self.health_ -= damage

    def attack(self):
        return self.attack_

    def dodgeChance(self):
        return random.randrange(1, self.dodgeChance_, 3)

    def getName(self):
        return self.name_
    name_ = ""
    health_ = 100
    attack_ = 0
    dodgeChance_ = 0