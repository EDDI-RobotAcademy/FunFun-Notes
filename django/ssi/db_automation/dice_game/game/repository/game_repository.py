from abc import ABC, abstractmethod

class GameRepository(ABC):

    @abstractmethod
    def create(self, gameCount):
        pass