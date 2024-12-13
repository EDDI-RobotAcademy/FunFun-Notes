from abc import ABC, abstractmethod


class ItemRepository(ABC):

    @abstractmethod
    def itemlist(self):
        pass