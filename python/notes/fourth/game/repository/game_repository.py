from abc import ABC, abstractmethod


class GameRepository(ABC):

    @abstractmethod
    def start(self, playerNameList, eachPlayerDiceList):
        pass

    @abstractmethod
    def checkWinner(self):
        pass
