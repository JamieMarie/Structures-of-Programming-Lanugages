import random
from monster import person
from monster import zombie
from monster import vampire
from monster import ghoul
from monster import werewolf
from observer import Observer
from observable import Observable

class Home(Observer, Observable):

    def __init__(self):
        self.mstrAmt = random.randint(1,10)
        #print "You should have {} monsters.".format(self.mstrAmt - 1)
        self.monsterList = [None] * self.mstrAmt
        self.generateMonsters(self.mstrAmt)

    def generateMonsters(self, mstrAmt):
        for i in range(1, mstrAmt):
            generator = random.randint(1,4)
            #print "GENERATOR #", generator
            if generator == 1:
                #Ghoul
                self.monsterList[i] = ghoul()
            elif generator == 2:
                #Vampire
                self.monsterList[i] = vampire()
            elif generator == 3:
                #Zombie
                self.monsterList[i] = zombie()
            else:
                #Werewolf
                self.monsterList[i] = werewolf()

    def getmstrAmt(self):
        return self.mstrAmt

    def setmstrAmt(self, mstrAmt):
        self.mstrAmt = mstrAmt

    def update(self):
        wut = False
        for i in range(1, len(self.monsterList)):
            death = self.monsterList[i].isDead()
            for j in range(1, len(self.monsterList)):
                if (not self.monsterList[j].name != "Person"):
                    wut = True
                else:
                    wut = False
                    #TODO print when no more monsters

    def getMonsters(self):
        return self.monsterList

    def isEmpty(self):
        for i in range(1, len(self.monsterList)):
            if self.monsterList[i].getName() is not "Person":
                return False
        return True

    def monsterNames(self):
        monsterNames = []
        for i in range(1, len(self.monsterList)):
            monsterNames.append(self.monsterList[i].name)
        return monsterNames

    def printMonsters(self):
        for i in range(1, len(self.monsterList)):
                self.monsterList[i].toStr()

    def attackHouse(self, damage):
        for i in range(1, len(self.monsterList)):
            if(self.monsterList[i].name != "Person"):
                self.monsterList[i].beAttacked(damage)
            else:
                print "You cannot attack a person..."
            #if (self.monsterList[i].name == "Person"):
            #    print "There's a person here! They gave you one point of health."
        self.update()

#print "am i done yet? No. :( "
#homie = Home()
#homie.printMonsters()
#homie.attackHouse(100)
#homie.printMonsters()
#homie.attackHouse(100)
#homie = Home()
#homie.printMonsters()
#print homie.monsterNames()
