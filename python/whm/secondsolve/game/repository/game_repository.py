from abc import ABC, abstractmethod

class GameRepository(ABC):

    @abstractmethod
    def setplayerIndexDiceGameMap(self,playerIndexLsit,diceIdList):
        pass

    @abstractmethod
    def updatePlayerIndexListMap(self,skillAppliedPlayerIndexList,secondDiceIdList):
        pass

    @abstractmethod
    def deleteTargetPlayerId(self,targetPlayerId):
        pass