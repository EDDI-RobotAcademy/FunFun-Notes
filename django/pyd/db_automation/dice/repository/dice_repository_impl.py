import random

from django.forms.models import model_to_dict

from dice.entity.dice import Dice
from dice.repository.dice_repository import DiceRepository


class DiceRepositoryImpl(DiceRepository):
    __instance = None

    MIN = 1
    MAX = 6

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        cls.__instance.__diceRepository = DiceRepositoryImpl.getinstance()
        return cls.__instance

    @classmethod
    def getinstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance


    def create(self):
        randomNumber = random.randint(self.MIN, self.MAX)
        dice = Dice(number=randomNumber)
        dice.save()

        return model_to_dict(dice)

    def findById(self,id):
        return Dice.objects.get(id=id)
