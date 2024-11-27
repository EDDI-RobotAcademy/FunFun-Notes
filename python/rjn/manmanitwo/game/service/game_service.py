
from abc import ABC, abstractmethod

class GameService(ABC):
    @abstractmethod
    def cardGameStart(self):
        pass
    @abstractmethod
    def gameRecord(self):
        pass