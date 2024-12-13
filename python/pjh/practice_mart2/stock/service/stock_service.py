from abc import ABC, abstractmethod


class StockService(ABC):

    @abstractmethod
    def addItem(self):
        pass