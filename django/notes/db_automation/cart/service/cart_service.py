from abc import ABC, abstractmethod


class CartService(ABC):

    @abstractmethod
    def createCart(self, accountId, cart):
        pass
