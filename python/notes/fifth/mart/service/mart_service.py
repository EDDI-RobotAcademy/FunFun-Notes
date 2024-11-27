from abc import ABC, abstractmethod


class MartService(ABC):

    @abstractmethod
    def loadFruit(self, fruitName, fruitCount):
        pass

    @abstractmethod
    def fruitMapList(self):
        pass

