from abc import ABC, abstractmethod


class OrderRepository(ABC):

    @abstractmethod
    def createOrder(self, fruit, count):
        pass