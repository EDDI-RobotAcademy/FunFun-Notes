from abc import ABC, abstractmethod


class OrderRepository(ABC):

    @abstractmethod
    def orderItem(self):
        pass
