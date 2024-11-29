from abc import ABC, abstractmethod


class MartRepository(ABC):

    @abstractmethod
    def addFruit(self,fruitName,fruitAmount):
        pass
    @abstractmethod
    def printCurrentStatus(self):
        pass