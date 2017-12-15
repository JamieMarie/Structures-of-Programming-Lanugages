import random
from weapon import HersheyKiss
from weapon import ChocolateBar
from weapon import SourStraw
from weapon import NerdBomb
from weapon import weapon

class Player(object):
    def __init__(self):
        self.health = 200
        self.attackLevel = random.randrange(10, 20)
        self.inventory = [None] * 11
        self.generateWeapons()

    def generateWeapons(self):
        for i in range(1, 11):
            generator = random.randrange(1,5)
            if generator == 1:
                #Kiss
                self.inventory[i] = HersheyKiss()
            elif generator == 2:
                #Straw
                self.inventory[i] = SourStraw()
            elif generator == 3:
                #ChocolateBar
                self.inventory[i] = ChocolateBar()
            else:
                #NerdBomb
                self.inventory[i] = NerdBomb()

            self.inventory[i].applyModifier(self.attackLevel)

    def takeDamage(self, damage):
        self.health -= damage

    def setInventory(self):
        self.inventory[0] = HersheyKisses()
        self.inventory[0].setAttackModifier(round(self.inventory[0].getAttack() * self.attackLevel, 2))
        for i in range (1, len(self.inventory)):
            temp = [ChocolateBar(), SourStraw(), NerdBomb()]
            self.inventory[i] = temp[randint(0,2)]
            self.inventory[i].setAttackModifier(round(self.inventory[i].getAttack() * self.attackLevel, 2))

    def getHealth(self):
        return self.health

    def updateInventory(self):
        for i in range(len(self.inventory)):
            if self.inventory[i].remaining == 0:
                del self.inventory[i]
                return

    def clearInventory(self):
        self.inventory = [None] * 11

    def getAttack(self):
        return self.attackLevel

    def getInventory(self):
        return self.inventory

    def searchInventory(self, name):
        for i in range(1, len(self.inventory)):
            if self.inventory[i].name == name:
                return True
        return False

    def returnItem(self, name):
        for i in range(1, len(self.inventory)):
            if self.inventory[i].name == name:
                return self.inventory[i]
        return None

    def useItem(self, name):
        for i in range(1, len(self.inventory)):
            if self.inventory[i].name == name:
                self.inventory[i].useWeapon()
                self.updateInventory()

    def printInventory(self):
        print ("\nYou have the following items: \n")
        for i in range(1, len(self.inventory)):
            print self.inventory[i].toStr(), "\t"
