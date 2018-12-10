from ClassDescriptions.Character import *


class Cowboy(Character):
    def __init__(self, name, health, damage):
        self.name = name
        self.HP = health
        self.DMG = damage
        Character.__init__(self, self.name, self.HP, self.DMG)
