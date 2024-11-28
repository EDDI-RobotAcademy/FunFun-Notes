from abc import ABC, abstractmethod


class ConsoleUiRepository(ABC):

    @abstractmethod
    def printMessage(self, state):
        pass

    @abstractmethod
    def processUserInput(self, state):
        pass
