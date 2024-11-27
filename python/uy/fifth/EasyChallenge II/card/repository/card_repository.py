from abc import ABC, abstractmethod

class CardRepository(ABC):

    @abstractmethod
    def pickCard(self):
        pass