import random
from abc import ABCMeta, abstractmethod
from observable import Observable

class monster(Observable):

    def __init__(self):
        self.name = ""
        self.attack = 0
        self.hp = 0

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getAttack(self):
        return self.name

    def getHp(self):
        return self.hp

    def setHp(self, hp):
        self.hp = hp

    def toStr(self):
        print "Name: ", self.name
        print "Attack Value: ", self.attack
        print "Health: ", self.hp

    def beAttacked(self, attackVal):
        if(self.name != "Person"):
            self.hp -= attackVal
            if(self.hp < 0):
                self.hp = 0
            result = self.isDead()
            if(result == False):
                print "{} attacked. Lost {} health. Now has {} hp.".format(self.name, attackVal, self.hp)

    def isDead(self):
        if(self.hp == 0):
            print "{} attacked. It is now dead!".format(self.name)
            self.hp = 999
            self.attack = -1
            self.name = "Person"
            return True
        return False

class person(monster):
    def __init__(self):
        self.hp = 9999
        self.attack = -1
        self.name = "Person"

class zombie(monster):
    def __init__(self):
        self.hp = random.randint(50,100)
        self.attack = random.randint(0,10)
        self.name = "Zombie"

class vampire(monster):
    def __init__(self):
        self.hp = random.randint(100,200)
        self.attack = random.randint(10,20)
        self.name = "Vampire"

class ghoul(monster):
    def __init__(self):
        self.hp = random.randint(40,80)
        self.attack = random.randint(15,30)
        self.name = "Ghoul"

class werewolf(monster):
    def __init__(self):
        self.hp = 200
        self.attack = random.randint(0,40)
        self.name = "Werewolf"
