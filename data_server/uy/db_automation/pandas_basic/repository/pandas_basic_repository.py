from abc import ABC, abstractmethod


class PandasBasicRepository(ABC):

    @abstractmethod
    def createMany(self, dataList):
        pass