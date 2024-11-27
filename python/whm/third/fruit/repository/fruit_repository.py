from abc import ABC, abstractmethod

class FruitRepository(ABC):

    @abstractmethod
    def createFruit(self):
        pass

    @abstractmethod
    def AllList(self):
        pass