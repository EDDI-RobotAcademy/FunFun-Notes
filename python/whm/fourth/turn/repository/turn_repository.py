from abc import ABC, abstractmethod

class TurnRepository(ABC):

    @abstractmethod
    def selectTurn(self):
        pass