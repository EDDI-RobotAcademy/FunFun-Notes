from abc import ABC, abstractmethod


class BlogPostService(ABC):

    @abstractmethod
    def requestCreate(self, title, content, accountId):
        pass
