from abc import ABC, abstractmethod


class GameService(ABC):

    @abstractmethod
    def startDiceGame(self):
        pass

    @abstractmethod
    def rollFirstDice(self):
        pass

    @abstractmethod
    def rollSecondDice(self):
        pass

    @abstractmethod
    def checkWinner(self):
        pass
