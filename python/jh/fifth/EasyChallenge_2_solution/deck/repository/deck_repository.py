from abc import ABC, abstractmethod


class DeckRepository(ABC):

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def drawCard(self):
        pass
