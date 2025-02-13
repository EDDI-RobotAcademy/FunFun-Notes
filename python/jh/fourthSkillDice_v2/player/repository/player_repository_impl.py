from player.entity.player import Player
from player.repository.player_repository import PlayerRepository


class PlayerRepositoryImpl(PlayerRepository):

    __instance = None
    __playerList = []

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
        userInputName = input("Input player Name you want to create: ")
        return userInputName

    def createName(self):
        userInputPlayerName = self.__processUserInput()
        player = Player(userInputPlayerName)

        self.__playerList.append(player)

    def getPlayerList(self):
        return self.__playerList

    def findByPlayerId(self, playerId):
        for player in self.__playerList:
            if player.getId() == playerId:
                return player


