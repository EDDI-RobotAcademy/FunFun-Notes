from abc import ABC, abstractmethod


class BuyerService(ABC):

    @abstractmethod
    def buyFruit(self, fruitName, fruitCount):
        pass

