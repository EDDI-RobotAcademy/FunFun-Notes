from abc import ABC, abstractmethod

class TurnRepository(ABC):

    @abstractmethod
    def selectTurn(self):
        pass

    @abstractmethod
    def createTrun(self):
        pass
    @abstractmethod
    def addTurn(self):
        pass
