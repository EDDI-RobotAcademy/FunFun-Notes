#from django.forms import model_to_dict

from dice_game.game.entity.game import Game
from dice_game.game.repository.game_repository import GameRepository


class GameRepositoryImpl(GameRepository):
    __instance = None
    __game=None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance


    def create(self,gameCount):
        game=Game(gameCount=gameCount)
        self.__game=game