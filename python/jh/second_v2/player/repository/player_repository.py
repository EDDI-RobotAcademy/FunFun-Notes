from abc import ABC, abstractmethod


class PlayerRepository(ABC):

    @abstractmethod
    def rollPlayerDiceList(self):
        pass
