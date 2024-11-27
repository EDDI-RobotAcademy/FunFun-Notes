from abc import ABC, abstractmethod


class BuyerRepository(ABC):

    @abstractmethod
    def buyerlist(self):
        pass
