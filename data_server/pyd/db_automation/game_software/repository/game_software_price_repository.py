from abc import ABC, abstractmethod


class GameSoftwarePriceRepository(ABC):

    @abstractmethod
    def create(self, gameSoftware, price):
        pass