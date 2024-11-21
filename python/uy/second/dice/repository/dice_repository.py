from abc import ABC, abstractmethod

# 행동

class DiceRepository(ABC):

    @abstractmethod
    def rollDice(self):
        pass