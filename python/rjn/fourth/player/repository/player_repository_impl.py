import random

from player.entity.player import Player
from player.repository.player_repository import PlayerRepository


class PlayerRepositoryImpl(PlayerRepository):
    __instance = None

    __playerNameList = []

    MIN = 0
    MAX = 2

    #
    # singleton
    #
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance


    #
    # input박스 생성, 입력받은 playerName 반환
    #
    def __processUserInput(self):
        userInputName = input("생성하고자 하는 이름을 입력하세요: ")
        return userInputName

    #
    # Player entity에 input메서드에서 반환받은 playerName전달
    #
    def createName(self):
        userInputPlayerName = self.__processUserInput()
        player = Player(userInputPlayerName)

        # 두번 입력한 playName을 list에 전달
        self.__playerNameList.append(player)

    #
    #
    #
    def acquirePlayerNameList(self):
        return self.__playerNameList
    