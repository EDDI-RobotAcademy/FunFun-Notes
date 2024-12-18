from abc import ABC, abstractmethod


class GameSoftwareService(GameSoftwareService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__gameSoftwareRepository = GameSoftwareRepositorImpl.getinstance()
        return cls.__instance
    @abstractmethod
    def createGameSoftwareToDatabase(self):
        pass