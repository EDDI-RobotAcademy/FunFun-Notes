from abc import ABC, abstractmethod


class StockRepository(ABC):

    @abstractmethod
    def orderItem(self):
        pass

    @abstractmethod
    def updateStockList(self):
        pass