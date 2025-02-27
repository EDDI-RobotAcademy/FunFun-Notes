from abc import ABC, abstractmethod


class CrawlRepository(ABC):

    @abstractmethod
    def crawl(self):
        pass
