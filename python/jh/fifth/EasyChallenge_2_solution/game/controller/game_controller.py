from abc import ABC, abstractmethod


class GameController(ABC):

    @abstractmethod
    def launchGame(self):
        pass
