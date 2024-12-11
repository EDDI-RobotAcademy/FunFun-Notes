import random

from player.entity.player import Player
from player.repository.player_repository import PlayerRepository


class PlayerRepositoryImpl(PlayerRepository):
    __instance = None

    __playerNicknameList = ["test01", "test02", "test03"]

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def rollPlayerNicknameList(self):
        playerNickname = random.randint(0, 2)
        player = Player(playerNickname)
        self.__playerNicknameList.append(player)
        print(f"result: {self.__playerNicknameList}")

    def acquirePlayerNicknameList(self):
        return self.__playerNicknameList