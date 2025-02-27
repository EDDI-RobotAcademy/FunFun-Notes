from abc import ABC, abstractmethod


class GameSoftwareImageRepository(ABC):

    @abstractmethod
    def create(self, gameSoftware, image):
        pass