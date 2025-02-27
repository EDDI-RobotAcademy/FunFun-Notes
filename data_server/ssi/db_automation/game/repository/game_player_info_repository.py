from abc import ABC, abstractmethod


class GamePlayerInfoRepository(ABC):

    @abstractmethod
    def create(self, game, player):
        pass

    @abstractmethod
    def findById(self, id):
        pass

    @abstractmethod
    def findByGame(self, game):
        pass
