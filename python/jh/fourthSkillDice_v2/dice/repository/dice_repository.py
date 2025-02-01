from abc import ABC, abstractmethod

class DiceRepository(ABC):

    @classmethod
    def rollDice(self):
        pass

    @classmethod
    def findByDiceId(self, diceId):
        pass