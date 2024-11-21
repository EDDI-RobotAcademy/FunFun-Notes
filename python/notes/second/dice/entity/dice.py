import random


class Dice:
    MAX = 6
    MIN = 1

    def __init__(self):
        self.__number = 0

    def rollDice(self):
        self.__number = random.randint(self.MIN, self.MAX)

    def printResult(self):
        print(f"dice number: {self.__number}")
