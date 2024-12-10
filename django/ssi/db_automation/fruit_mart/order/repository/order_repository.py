from abc import ABC, abstractmethod

class OrderRepository(ABC):

    @abstractmethod
    def getInstance(cls):
        pass

    @abstractmethod
    def create(self, customer, fruit, quantity):
        pass

    @abstractmethod
    def find_all(self):
        pass

    @abstractmethod
    def find_by_customer(self, customer_name):
        pass

    @abstractmethod
    def find_by_order_id(self, order_id):
        pass



