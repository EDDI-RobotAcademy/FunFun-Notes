from abc import ABC, abstractmethod


class TwoDiceRepository(ABC):

    @abstractmethod
    def rollDice(self):
        pass