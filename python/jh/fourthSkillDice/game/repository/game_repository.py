from abc import ABC, abstractmethod


class GameRepository(ABC):

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def setPlayerIndexListToMap(self, playerIndexList, diceIdList):
        pass

    @abstractmethod
    def updatePlayerDiceGameMap(self, skillAppliedPlayerIndexList, secondDiceIdList):
        pass

    @abstractmethod
    def deletePlayer(self, tagetPlayerId):
        pass

        # 이렇게 하면 에러 남
    # @abstractmethod
    # def setPlayerIndextListToMap(self):
    #     pass
