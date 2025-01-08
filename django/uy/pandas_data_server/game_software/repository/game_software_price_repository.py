from abc import ABC, abstractmethod


class GameSoftwarePriceRepository(ABC):

    @abstractmethod
    def create(self, gameSoftware, price):
        pass

    @abstractmethod
    def findByGameSoftware(self, gameSoftware):
        pass
