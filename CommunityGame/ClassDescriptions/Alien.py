import random


class Alien(object):
    def __init__(self, max_health=100, dmg_rolls=1, max_dmg=10, dmg_add=0 ):
        self.health = max_health
        self.max_health = max_health
        self.dmg_rolls = dmg_rolls
        self.max_dmg = max_dmg
        self.dmg_add = dmg_add

    def take_damage(self, damage=0):
        self.health -= damage

    def damage(self):
        dmg = 0
        for i in range(self.dmg_rolls):
            dmg += random.randint(1, self.max_dmg) + self.dmg_add
        return dmg

