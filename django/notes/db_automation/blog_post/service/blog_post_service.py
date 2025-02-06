from abc import ABC, abstractmethod


class BlogPostService(ABC):

    @abstractmethod
    def requestList(self, page, perPage):
        pass

    @abstractmethod
    def requestCreate(self, title, content, accountId):
        pass
