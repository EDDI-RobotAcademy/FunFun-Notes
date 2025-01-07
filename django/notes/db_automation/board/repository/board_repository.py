from abc import ABC, abstractmethod


class BoardRepository(ABC):

    @abstractmethod
    def list(self, page, perPage):
        pass

    @abstractmethod
    def save(self, board):
        pass