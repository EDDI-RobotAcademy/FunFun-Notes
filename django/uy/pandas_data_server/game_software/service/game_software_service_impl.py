from game_software.repository.game_software_repository_impl import GameSoftwareRepositoryImpl
from game_software.service.game_software_service import GameSoftwareService


class GameSoftwareServiceImpl(GameSoftwareService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__gameSoftwareRepository = GameSoftwareRepositoryImpl.getInstance()

            return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance


    def requestList(self, page, perPage):
        return self.__gameSoftwareRepository.list(page, perPage)