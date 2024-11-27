from abc import ABC, abstractmethod


class OrderRepository(ABC):

    @abstractmethod
    def create(self, fruitName, fruitCount, customerId):
        pass

    @abstractmethod
    def findOrderByCustomerId(self, customerId):
        pass