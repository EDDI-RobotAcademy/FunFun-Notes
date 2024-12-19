from abc import ABC, abstractmethod


class GameSoftwareService(ABC):

    @abstractmethod
    def requestList(self, page, perPage):
        pass

    @abstractmethod
    def createGameSoftware(self, title, price, description, image):
        pass