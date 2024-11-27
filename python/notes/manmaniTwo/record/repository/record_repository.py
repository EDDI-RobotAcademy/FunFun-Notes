from abc import ABC, abstractmethod


class RecordRepository(ABC):

    @abstractmethod
    def create(self, accountId, turnCountNumber, isWin):
        pass
