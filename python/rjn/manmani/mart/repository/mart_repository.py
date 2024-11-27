from abc import ABC, abstractmethod

from mart.entity.products import Products


class MartRepository(ABC):
    @abstractmethod
    def addProduct(self, name, count):
        pass

    @abstractmethod
    def reduceProduct(self, name, count):
        pass

    @abstractmethod
    def getAllProducts(self) -> list[Products]:
        pass