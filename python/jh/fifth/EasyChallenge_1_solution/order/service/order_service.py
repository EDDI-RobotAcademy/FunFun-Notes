from abc import ABC, abstractmethod


class OrderService(ABC):

    @abstractmethod
    def buyFruit(self, fruitName, fruitCount, customerId):
        pass

    @abstractmethod
    def orderList(self, customerId):
        pass
