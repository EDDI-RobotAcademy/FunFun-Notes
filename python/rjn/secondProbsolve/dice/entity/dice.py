import random


class Dice:

        MAX = 6
        MiN = 1

        def __init__(self, diceNumber):
            self.__number = diceNumber


        def printResult(self):
            print(f"dice number : {self.__number}")