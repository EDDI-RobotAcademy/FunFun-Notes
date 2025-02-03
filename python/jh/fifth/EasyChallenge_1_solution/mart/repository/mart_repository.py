from abc import ABC, abstractmethod


class MartRepository(ABC):

    @abstractmethod
    def create(self, fruitName, fruitCount):
        pass

    @abstractmethod
    def mapList(self):
        pass

    @abstractmethod
    def update(self, fruitName, quantity):
        pass
