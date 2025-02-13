from abc import ABC, abstractmethod


class ConsoleUiService(ABC):

    @abstractmethod
    def printMessage(self, state):
        pass

    @abstractmethod
    def processUserInput(self, currentState):
        pass
