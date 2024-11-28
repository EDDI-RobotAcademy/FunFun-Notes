from abc import ABC, abstractmethod


class ItemRepository(ABC):

    @abstractmethod
    def createItem(self):
        pass