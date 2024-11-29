import random

from django.forms import model_to_dict

from dice.entity.dice import Dice
from dice.repository.dice_repository import DiceRepository


class DiceRepositoryImpl(DiceRepository):
    __instance = None

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

    def create(self):
        randomNumber = random.randint(self.MIN, self.MAX)
        dice = Dice(number=randomNumber)
        dice.save()

        # return dice
        return model_to_dict(dice)
