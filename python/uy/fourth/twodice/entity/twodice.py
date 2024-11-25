import random

class TwoDice:
    #MAX = 6
    #MIN = 1

    def __init__(self, diceNumber):
        self.__diceNumber = diceNumber

    #def rollDice(self):
    #    self.__number = random.randint(self.MIN, self.MAX)

    def printResult(self):
        print(f"dice number: {self.__diceNumber}")

    def getDiceNumber(self):
        return self.__diceNumber

