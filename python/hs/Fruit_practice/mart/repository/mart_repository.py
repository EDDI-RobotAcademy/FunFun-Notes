from abc import ABC, abstractmethod

@abstractmethod
class MartRepository(ABC):

    def addFruit(self, fruitName, addAmount):
        pass

    def sellFruit(self, fruitName, sellAmount):
        pass

    def status(self):
        pass

