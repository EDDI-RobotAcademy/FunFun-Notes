from abc import ABC, abstractmethod

from inventory.entity.inventory import Inventory


class InventoryRepository(ABC):
    @abstractmethod
    def addProduct(self, namer, count):
        pass

    @abstractmethod
    def reduceProduct(self, name, count):
        pass

    @abstractmethod
    def getAllProducts(self) -> list[Inventory]:
        pass