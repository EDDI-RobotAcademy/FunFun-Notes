from abc import ABC, abstractmethod

class GameRepository(ABC):

    @abstractmethod
    def start(self):
        pass
