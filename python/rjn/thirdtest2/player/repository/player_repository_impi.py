import random

from player.entity.player import Player
from player.repository.player_repository import PlayerRepository


class PlayerRepositoryImpl(PlayerRepository):

    __instance = None

    __plyerList = ['AAA', 'BBB', 'CCC','DDD','EEE']

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance
    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def pickName(self):
        playerName = random.choice(self.__plyerList)
        name = Player(playerName)
        return name

