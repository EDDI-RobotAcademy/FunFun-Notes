from abc import ABC, abstractmethod


class CarService(ABC):

    @abstractmethod
    def crawlCarData(self):
        pass

    @abstractmethod
    def carList(self):
        pass

    @abstractmethod
    def requestModifyCarText(self):
        pass
