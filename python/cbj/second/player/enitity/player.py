import random

class Player:
    MAX = 1
    MIN = 1

    def __init__(self):
        self.__number = 0

    def rollPlayer(self):
        self.__number = random.randint(self.MIN, self.MAX)

    def printResult(self):
        print(f"player number: {self.__number}")