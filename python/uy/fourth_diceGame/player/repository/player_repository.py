from abc import ABC, abstractmethod

class PlayerRepository(ABC):

    @abstractmethod
    def createName(self, playerName):
        pass

    def getUserList(self):
        pass