import random

from dice.entity.dice import Dice
from dice.repository.dice_repository import DiceRepository


class DiceRepositoryImpl(DiceRepository):
    __instance = None
    #instance 생성

    MIN = 1
    MAX = 6

    def __new__(cls):
        #진짜 생성자 생성
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def rollDice(self):
        diceNumber = random.randint(self.MIN, self.MAX)
        dice = Dice(diceNumber)
        return dice.getDiceNumber()
