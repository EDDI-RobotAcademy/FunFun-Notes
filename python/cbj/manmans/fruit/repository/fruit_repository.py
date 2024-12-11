from abc import ABC, abstractmethod


class FruitRepository(ABC):

    @abstractmethod
    def create(self, fruitName, fruitCount):
        pass