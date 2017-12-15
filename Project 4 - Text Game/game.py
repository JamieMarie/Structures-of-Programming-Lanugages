import sys
from player import Player
from neighborhood import Neighborhood

class Game:
    def __init__(self):
        self.myPlayer = Player()
        self.grid = Neighborhood()
        self.houseNums = [0,0]
        self.currentHouse = self.grid.getHouse(self.houseNums[0], self.houseNums[1])
        self.message = None
        self.displayOpening()
        self.playGame()

    def displayOpening(self):
        print "\n\n\n\n\n\n\n\n"
        print "================================================================"
        print "               WELCOME TO A REALLY SILLY GAME"
        print "================================================================"
        print "It seemed like a normal Halloween Eve. You bought a lot of "
        print "candy, ate a lot of candy, and went to bed early. You had a lot"
        print "trick-or-treating to do the next day."
        print "Unfortunately, when you woke up you discovered that the world "
        print "was not how you left it. Batches of bad candy had transformed "
        print "your friends and neighbors into all sorts of crazy monsters. "
        print "Somehow you missed the tainted candy; it is therefore up to you"
        print "to save your neighborhood and turn everyone back to normal."
        print "================================================================"
        print "                Your available actions are:"
        print "         - Move                           - Inventory"
        print "           - Left                         - Attack"
        print "           - Right                        - Flee"
        print "           - Down                         - Inhabitants"
        print "           - Up                           "
        print "                For any questions, type Help."
        print "                   Have fun and good luck!!"
        print "================================================================"
        print ""

    def playGame(self):
        alive = True
        while alive:
            if self.myPlayer.health <= 0:
                print ("You are dead.")
                print "Please play again...if you dare!"
                break
            if self.grid.gameWon() == True:
                print ("You defeated all of the monsters!")
                break
            print ("Your coordinates are: " + str(self.houseNums[0]) + "," + str(self.houseNums[1]))
            s = raw_input("What would you like to do? ")
            self.getInput(s)

    def attackHouse(self):
        finished = False

        while finished is False:
            w = raw_input("What weapon would you like to use? ")
            if w.lower() == "exit":
                return

            if w == "Chocolate Bar":
                if self.myPlayer.searchInventory(w):
                    tempItem = self.myPlayer.returnItem(w)
                    attackingVal = tempItem.attack
                    self.currentHouse.attackHouse(attackingVal)
                    #self.myPlayer.useItem(w)
                    break
                else:
                    print "You don't have this item."
            elif w == "Sour Straw":
                if self.myPlayer.searchInventory(w):
                    tempItem = self.myPlayer.returnItem(w)
                    attackingVal = tempItem.attack
                    self.currentHouse.attackHouse(attackingVal)
                    #self.myPlayer.useItem(w)
                    break
                else:
                    print "You don't have this item."
            elif w == "Hershey Kiss":
                if self.myPlayer.searchInventory(w):
                    tempItem = self.myPlayer.returnItem(w)
                    attackingVal = tempItem.attack
                    self.currentHouse.attackHouse(attackingVal)
                    #self.myPlayer.useItem(w)
                    break
                else:
                    print "You don't have this item."
            elif w == "Nerd Bomb":
                if self.myPlayer.searchInventory(w):
                    tempItem = self.myPlayer.returnItem(w)
                    attackingVal = tempItem.attack
                    self.currentHouse.attackHouse(attackingVal)
                    #self.myPlayer.useItem(w)
                    break
                else:
                    print "You don't have this item."
            else:
                print "Please enter a valid weapon. Maybe check your inventory first."
                print "Also make sure you enter the name right. (ex. Sour Straw not sour straw)"


            #tempWeapon = self.checkWeaponInput(w)
            #finished = self.myPlayer.attackHouse(self.currentHouse, tempWeapon)
        #self.currentHouse.attackPlayer(self.myPlayer)
        #print ("Current health: ", self.myPlayer.getHealth())

    def checkWeaponInput(self, w):
        w = w.lower()
        for i in self.myPlayer.inventory:
            if i.name.lower() == w:
                return i.name

        return None

    def checkMove(self):
        while True:
            m = raw_input("What direction would you like to move? ")
            m = m.lower()
            if m == "left":
                if self.houseNums[0] <= 0:
                    print ("You can't go further left.")
                else:
                    self.houseNums[0] -= 1
                    break

            elif m == "right":
                if self.houseNums[0] >= self.grid.getMax()-1:
                    print ("You can't go further right.")
                else:
                    self.houseNums[0] += 1
                    break

            elif m == "up":
                if self.houseNums[1] <= 0:
                    print ("You can't go further up.")
                else:
                    self.houseNums[1] -= 1
                    break

            elif m == "down":
                if self.houseNums[1] >= self.grid.getMax()-1:
                    print ("You can't go further down.")
                else:
                    self.houseNums[1] += 1
                    break

            elif m == "exit":
                break

            else:
                print ("That wasn't a valid direction! Try up, down, left, right...")


    def getInput(self, n):
        n = n.lower()
        if n == "help":
            print "================================================================"
            print "Your goal is to kill all the monsters. Try moving around to find"
            print "some to attack. The layout of your commands should look a little"
            print "like this:"
            print "          What would you like to do? Move"
            print "          What would you like to do? Attack"
            print "          What would you like to do? Inventory"
            print "\n        If you're still confused, probs just give up."
            print "================================================================"
            print "\n\n\n\n\n\n\n\n\n\n\n"

        elif n == "inventory":
            self.myPlayer.printInventory()

        elif n == "attack":
            self.attackHouse()

        elif n == "move":
            self.checkMove()
            self.currentHouse = self.grid.getHouse(self.houseNums[0], self.houseNums[1])

        elif n == "inhabitants":
            print "The inhabitants of this house are:\n", self.currentHouse.printMonsters()

        elif n == "flee":
            sys.exit("Fly, you fool!\nYou have exited and lost the game.")

        else:
            if (len(n) > 0):
                print ("Invalid thing!")

    def getLocation(self):
        return self.houseNums

if __name__ == "__main__":
    game = Game()
