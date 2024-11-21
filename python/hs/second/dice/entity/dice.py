import random

class Dice:
    max = 6
    min = 1

    def __init__(self):
        self.__number = 0

    def rollDice(self):
        self.__number = random.randint(self.min, self.max)

    def printResult(self):
        print(f"dice number: {self.__number}")
