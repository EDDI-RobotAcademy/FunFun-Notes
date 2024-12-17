from abc import ABC, abstractmethod


class PandasBasicService(ABC):
    @abstractmethod
    def createPandasInfo(self):
        pass

    @abstractmethod
    def pandasInfoList(self):
        pass

    @abstractmethod
    def paginatedPandasInfoList(self, page, perPage):
        pass

    @abstractmethod
    def statisticsSummary(self):
        pass

    @abstractmethod
    def filteredPandasInfo(self, filteredDictionary):
        pass