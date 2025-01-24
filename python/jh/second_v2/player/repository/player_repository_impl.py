import random
from player.entity.player import PlayerDice
from player.repository.player_repository import PlayerRepository


class PlayerRepositoryImpl(PlayerRepository):
    __instance =None

    __playerDiceList = []


    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def rollPlayerDiceList(self):
        playerDiceNum = random.randint(0,6)
        playerDice = PlayerDice(playerDiceNum)
        self.__playerDiceList.append(playerDice)


    def acquirePlayerDiceList(self):
        return self.__playerDiceList






