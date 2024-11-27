from abc import ABC, abstractmethod

class CardRepository(ABC):

    @abstractmethod
    def selectCard(self):
        pass