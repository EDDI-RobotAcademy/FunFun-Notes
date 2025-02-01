from game.entity.game import Game
from game.repository.game_repository import GameRepository


class GameRepositoryImpl(GameRepository):
    __instance = None

    __game = None


    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def create(self):
        while True:
            try:
                playerCount = int(input("How many player?: "))
                if playerCount <= 1:
                    print("The number of players must be at least Two!")
                    continue

                game = Game(playerCount)
                self.__game = game

                break

            except ValueError:
                print("Input only Number!")


    def getGamePlayerCount(self):
         return self.__game.getPlayerCount()

    def setPlayerIndexListToMap(self, playerIndexList, diceIdList):
        return self.__game.setPlayerIndexListToMap(playerIndexList, diceIdList)

    def updatePlayerDiceGameMap(self, playerIndexList, diceIdList):
        return  self.__game.updatePlayerIndexListToMap(playerIndexList, diceIdList)

    def deletePlayer(self, deathShotTargetPlayerId):
        return self.__game.deleteTargetPlayerId(deathShotTargetPlayerId)

    def getGame(self):
        return self.__game


