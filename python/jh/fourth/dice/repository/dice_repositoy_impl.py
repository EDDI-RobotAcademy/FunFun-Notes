import random

from dice.entity.dice import Dice
from dice.repository.dice_repositoy import DiceRepository


class DiceRepositoryImpl(DiceRepository):
    __instance = None
    __diceList = []

    MIN = 1
    MAX = 6


    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def rollDice(self):
        diceNum = random.randint(self.MIN,self.MAX)
        dice = Dice(diceNum)
        self.__diceList.append(dice)

    def getDiceList(self):
        return self.__diceList


