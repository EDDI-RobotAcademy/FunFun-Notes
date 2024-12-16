from abc import ABC, abstractmethod


class PlayerRepository(ABC):

    @abstractmethod
    def create(self, nickname):
        pass

    @abstractmethod
    def findById(self, id):
        pass
    