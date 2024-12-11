from abc import ABC, abstractmethod


class GameServiceRepository(ABC):

    @abstractmethod
    def checkWinner(self):
        pass