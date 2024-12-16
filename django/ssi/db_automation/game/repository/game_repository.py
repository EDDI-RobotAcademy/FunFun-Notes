from abc import ABC, abstractmethod


class GameRepository(ABC):

    @abstractmethod
    def create(self, playerCount):
        pass

    @abstractmethod
    def findById(self, id):
        pass

    @abstractmethod
    def update(self, game, gameState):
        pass
