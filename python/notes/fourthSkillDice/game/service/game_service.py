from abc import ABC, abstractmethod


class GameService(ABC):

    @abstractmethod
    def startDiceGame(self):
        pass

    @abstractmethod
    def printCurrentStatus(self):
        pass

    @abstractmethod
    def rollFirstDice(self):
        pass

    @abstractmethod
    def rollSecondDice(self):
        pass

    @abstractmethod
    def applySkill(self):
        pass

    @abstractmethod
    def checkWinner(self):
        pass
