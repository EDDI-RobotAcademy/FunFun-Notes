from dice.entity.dice_skill import DiceSkill
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

    def create(self, playerCount):
        game = Game(playerCount)
        self.__game = game

    def setPlayerIndexListToMap(self, playerIndexList, diceIdList):
        self.__game.setPlayerIndexListToMap(playerIndexList, diceIdList)

    def updatePlayerDiceGameMap(self, skillAppliedPlayerIndexList, secondDiceIdList):
        self.__game.updatePlayerIndexListToMap(skillAppliedPlayerIndexList, secondDiceIdList)

    def deletePlayer(self, tagetPlayerId):
        self.__game.deleteTargetPlayerId(tagetPlayerId)

    def getGamePlayerCount(self):
        return self.__game.getPlayerCount()

    def getGame(self):
        return self.__game
        
