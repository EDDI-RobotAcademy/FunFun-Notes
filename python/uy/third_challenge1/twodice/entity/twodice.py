import random

class TwoDice:
    #MAX = 6
    #MIN = 1

    def __init__(self, number):
        self.__number = number

    #def rollDice(self):
    #    self.__number = random.randint(self.MIN, self.MAX)

    def printResult(self):
        print(f"dice number: {self.__number}")

    def getDiceNumber(self):
        return self.__number

