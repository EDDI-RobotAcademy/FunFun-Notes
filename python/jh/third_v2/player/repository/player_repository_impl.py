import random

from player.entity.player import Player
from player.repository.player_repository import PlayerRepository


class PlayerRepositoryImpl(PlayerRepository):
    __instance = None

    __playerNameSet = ["C-Language", "Python", "Java", "Go-Language", "Java-Script", "Dart"]
    __playerNameList = []



    MIN = 0
    MAX = 5

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
        selectIndex = random.randint(self.MIN,self.MAX)
        pickName = self.__playerNameSet[selectIndex]

        return pickName

    def createName(self):
        selectedPlayerName = self.pickRandomName()
        player = Player(selectedPlayerName)

        self.__playerNameList.append(player)


    def acquirePlayerNameList(self):
        return self.__playerNameList
