from abc import ABC, abstractmethod


class GameService(ABC):

    @abstractmethod
    def createGame(self, playerCount):
        pass

    @abstractmethod
    def calculateWinner(self, gameId):
        pass

    @abstractmethod
    def requestInfo(self, gameId):
        pass
