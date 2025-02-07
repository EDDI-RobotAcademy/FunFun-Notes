from abc import ABC, abstractmethod

class DiceRepository(ABC):

    @abstractmethod
    def rollMultiDice(self):
        pass

