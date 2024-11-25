import random

from player.entity.player import Player
from player.repository.player_repository import PlayerRepository


class PlayerRepositoryImpl(PlayerRepository):
    __instance = None

    __playerName = ["Hello", "Hi", "Newbie"]
    __playerNameList = []

    MIN = 0
    MAX = 2

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def pickRandomName(self):
        selectedIndex = random.randint(self.MIN, self.MAX)
        return self.__playerName[selectedIndex]

    def createName(self):
        selectedPlayerName = self.pickRandomName()
        player = Player(selectedPlayerName)

        self.__playerNameList.append(player)

    def acquirePlayerNameList(self):
        return self.__playerNameList
    