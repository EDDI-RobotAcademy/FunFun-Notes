
from abc import ABC, abstractmethod

class GameRepository(ABC):
    @abstractmethod
    def recordGame(self):
        pass

    def getRecords(self):
        pass