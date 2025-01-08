from abc import ABC, abstractmethod


class BoardService(ABC):

    @abstractmethod
    def requestList(self, page, perPage):
        pass

    @abstractmethod
    def requestCreate(self, title, content, accountId):
        pass