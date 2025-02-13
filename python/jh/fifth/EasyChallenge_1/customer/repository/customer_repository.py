from abc import ABC, abstractmethod


class CustomerRepository(ABC):

    @abstractmethod
    def selectFruit(self):
        pass

    @abstractmethod
    def selectCount(self):
        pass


