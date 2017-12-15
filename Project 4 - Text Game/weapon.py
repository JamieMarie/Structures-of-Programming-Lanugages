import random

class weapon(object):

    def __init__(self):
        self.name = ""
        self.attack = 0
        self.remaining = 0

    def getName(self):
        return self.name

    def getAttack(self):
        return self.attack

    def applyModifier(self, value):
        self.attack = round((value * self.attack), 0)

    def getRemaining(self):
        return self.uses

    def useWeapon(self):
        self.remaining -= 1

    def toStr(self):
        print "Weapon: ", self.name
        print "Attack Value: ", self.attack
        print "Remaining Uses: ", self.remaining

class HersheyKiss(weapon):
    def __init__(self):
        self.name = "Hershey Kiss"
        self.attack = 1
        self.remaining = 999

class SourStraw(weapon):
    def __init__(self):
        self.name = "Sour Straw"
        self.attack = random.uniform(1, 1.75)
        self.remaining = 2

class ChocolateBar(weapon):
    def __init__(self):
        self.name = "Chocolate Bar"
        self.attack = random.uniform(2, 2.4)
        self.remaining = 4

class NerdBomb(weapon):
    def __init__(self):
        self.name = "Nerd Bomb"
        self.attack = random.uniform(3.5, 5)
        self.remaining = 1
