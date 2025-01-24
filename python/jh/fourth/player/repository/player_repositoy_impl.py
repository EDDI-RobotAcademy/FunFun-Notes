

from player.entity.player import Player
from player.repository.player_repositoy import PlayerRepository


class PlayerRepositoryImpl(PlayerRepository):

    __instance = None

    __playerNameList = []

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance


    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance


    def __processUserInput(self):
        userInputPlayerName = input("Input Your Name: ")
        return userInputPlayerName


    def createName(self):
        playerName = self.__processUserInput()
        player = Player(playerName)
        self.__playerNameList.append(player)


    def getPlayerNameList(self):
        return self.__playerNameList


