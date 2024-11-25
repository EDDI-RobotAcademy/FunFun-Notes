from abc import ABC, abstractmethod

class GameRepository(ABC):

    @abstractmethod
    def start(self, playerNameList, eachPlayerDiceNumber):
        pass

    @abstractmethod
    def checkWinner(self):
        pass
