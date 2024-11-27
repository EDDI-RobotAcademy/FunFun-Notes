from abc import ABC, abstractmethod


class PayService(ABC):

    @abstractmethod
    def createBillList(self):
        pass