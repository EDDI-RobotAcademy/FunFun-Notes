from abc import ABC, abstractmethod

class GameService(ABC):

    @abstractmethod
    def startGame(self):
        pass