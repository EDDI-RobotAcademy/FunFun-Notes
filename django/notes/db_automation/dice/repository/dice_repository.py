from abc import ABC, abstractmethod


class DiceRepository(ABC):

    @abstractmethod
    def create(self):
        pass
