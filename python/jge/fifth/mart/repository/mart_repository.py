from abc import ABC, abstractmethod
from mart.entity.mart import Item


class MartRepository(ABC):
    @abstractmethod
    def add_item(self, item: Item):
        pass

    @abstractmethod
    def get_item(self, name: str):
        pass

