from abc import ABC, abstractmethod


class PandasBasicRepository(ABC):
    @abstractmethod
    def createMany(self, dataList):
        pass

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def statistics(self, targetData):
        pass

    @abstractmethod
    def filterByCondition(self, ormFilteredDictionary):
        pass
