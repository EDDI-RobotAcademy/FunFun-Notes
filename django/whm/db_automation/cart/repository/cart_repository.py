from abc import ABC, abstractmethod


class CartRepository(ABC):

    @abstractmethod
    def save(self, cart):
        pass

    @abstractmethod
    def findCartByAccountAndGameSoftware(self, account, gameSoftware):
        pass

    @abstractmethod
    def findCartByAccount(self, account, offset, limit):
        pass

    @abstractmethod
    def deleteById(self, cartId):
        pass

    def findById(self, cartId):
        pass