from abc import ABC, abstractmethod


class AccountRepository(ABC):

    @abstractmethod
    def register(self, id, password):
        pass
