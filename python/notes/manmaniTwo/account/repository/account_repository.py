from abc import ABC, abstractmethod


class AccountRepository(ABC):

    @abstractmethod
    def register(self, accountId, password):
        pass

    @abstractmethod
    def login(self, accountId, password):
        pass

    @abstractmethod
    def findByAccountId(self, accountId):
        pass

    @abstractmethod
    def findById(self, id):
        pass
