from abc import ABC, abstractmethod

class MartService(ABC):

    @abstractmethod
    def createFruit(self):
        pass

    @abstractmethod
    def AllList(self):
        pass