from player.entity.player import Player
from player.repository.player_repository import player_Repository


class player_RepositoryImpl(player_Repository):

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

    def createName(self, username):
        player = Player(username)
        self.__playerList.append(player)

    def getUserList(self):
        return self.__playerList