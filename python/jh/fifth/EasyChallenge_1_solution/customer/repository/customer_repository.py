from abc import ABC, abstractmethod


class CustomerRepository(ABC):

    @abstractmethod
    def create(self, name):
        pass

    @abstractmethod
    def findById(self, id):
        pass
