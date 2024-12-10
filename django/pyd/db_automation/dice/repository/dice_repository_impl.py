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

    def create(self, game, player):
        randomNumber = random.randint(self.MIN, self.MAX)
        dice = Dice(number=randomNumber, game=game, player=player)
        dice.save()

        return model_to_dict(dice)

    def findById(self, id):
        return Dice.objects.get(id=id)

    def findByGameId(self, game):
        return Dice.objects.filter(game=game)

    def findAll(self):
        return Dice.objects.all()

    def findByGameAndPlayer(self, game, player):
        return Dice.objects.filter(game=game, player=player)
