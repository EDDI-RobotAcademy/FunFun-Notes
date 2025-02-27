from abc import ABC, abstractmethod


class OrderService(ABC):

    @abstractmethod
    def getInstance(cls):
        pass

    @abstractmethod
    def place_order(self, customer_name, fruit_name, quantity):
        pass