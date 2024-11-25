from abc import ABC, abstractmethod

class player_Repository(ABC):

    @abstractmethod
    def createName(self, username):
        pass

    @abstractmethod
    def getUserList(self):
        pass