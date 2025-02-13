from player.entity.player import Player
from player.repository.player_repository import PlayerRepository


class PlayerRepositoryImpl(PlayerRepository):
    __instance = None

    __playerNum = 0

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

    def __playerNum(self):
        self.__playerNum = int(input("플레이어의 인원수를 입력하세요: "))
        return self.__playerNum


    def __processUserInput(self):
        userInputName = input("생성하고자 하는 이름을 입력하세요: ")
        return userInputName

    def createNumAndName(self):
        playerNumber = self.__playerNum()

        for number in range(playerNumber):
            userInputPlayerName = self.__processUserInput()
            player = Player(userInputPlayerName)
            self.__playerNameList.append(player)

    def acquirePlayerNameList(self):
        return self.__playerNameList
