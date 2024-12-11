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
    def statisticsSummery(self):
        pass
