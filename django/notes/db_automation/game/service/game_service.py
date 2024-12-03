from abc import ABC, abstractmethod


class GameService(ABC):

    @abstractmethod
    def createGame(self):
        pass

    @abstractmethod
    def checkWinner(self, gameId):
        pass
