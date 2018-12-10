import random


class Character(object):
    def __init__(self, name, health = 100, damage=10):
        self.name = name
        self.HP = health
        self.DMG = damage
        # self.loc = location
        # self.inv = inventory

    def deal_dmg(self):
        dmg = random.randint(1, self.DMG)
        return dmg

    def

    def turn(self):




