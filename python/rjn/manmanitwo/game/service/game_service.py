
from abc import ABC, abstractmethod

class GameService(ABC):
    @abstractmethod
    def startCardGame(self):
        pass
    @abstractmethod
    def showGameRecords(self):
        pass