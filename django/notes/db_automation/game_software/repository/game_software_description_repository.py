from abc import ABC, abstractmethod


class GameSoftwareDescriptionRepository(ABC):

    @abstractmethod
    def create(self, gameSoftware, description):
        pass

    @abstractmethod
    def findByGameSoftware(self, gameSoftware):
        pass
