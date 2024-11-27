from abc import ABC, abstractmethod


class CustomerService(ABC):

    @abstractmethod
    def createCustomer(self, name):
        pass
