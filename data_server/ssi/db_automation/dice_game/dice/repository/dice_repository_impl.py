import random

from django.forms import model_to_dict

from dice_game.dice.entity.dice import Dice
from dice_game.dice.repository.dice_repository import DiceRepository


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

    def rollDice(self):
        randomNumber = random.randint(self.MIN, self.MAX)
        dice = Dice(number=randomNumber)
        dice.save()

        return model_to_dict(dice)

    def findById(self, id):
        return Dice.objects.get(id=id)


