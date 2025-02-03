import random

from dice.entity.dice import Dice
from dice.repository.dice_repository import DiceRepository


class DiceRepositoryImpl(DiceRepository):

    __instance = None

    __diceList = []

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
        diceNumber = random.randint(1,6)
        dice = Dice(diceNumber)
        self.__diceList.append(dice)

        return dice.getId()

    def findByDiceId(self, diceId):
        for dice in self.__diceList:
            if dice.getId() == diceId:
                return dice

    def getDiceList(self):
        return self.__diceList