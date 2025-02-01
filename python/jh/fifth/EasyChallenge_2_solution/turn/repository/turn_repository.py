from abc import ABC, abstractmethod


class TurnRepository(ABC):

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def addTurnCount(self):
        pass
