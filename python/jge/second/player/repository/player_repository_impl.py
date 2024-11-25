import random

from player.entity.player import Player
from player.repository.player_repository import PlayerRepository

class PlayerRepositoryImpl(PlayerRepository):
    __instance = None

    __nicknameList = ["test01", "test02", "test03"]

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def __selectRandomNickname(self):
        selectedIndex = random.randint(0, 2)
        return self.__nicknameList[selectedIndex]

    def pickYourRandomNickname(self):
        player = Player()
        selectedRandomNickname = self.__selectRandomNickname()

        player.setNickname(selectedRandomNickname)

        return player