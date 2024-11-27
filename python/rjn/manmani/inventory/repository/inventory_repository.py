from abc import ABC, abstractmethod

from inventory.entity.inventory import Inventory


class InventoryRepository(ABC):
    @abstractmethod
    def addProduct(self, name: str, count: int):
        pass

    @abstractmethod
    def reduceProduct(self, name: str, count: int):
        pass

    @abstractmethod
    def getAllProducts(self) -> list[Inventory]:
        pass