from game_software.repository.game_software_repository import ABC, abstractmethod


class GameSoftwareRepositoryImpl(GameSoftwareRepository):
    @abstractmethod
    def createMany(self, gameSoftwareList):
        pass