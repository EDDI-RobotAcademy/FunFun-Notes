from django.db import transaction

from game_software.repository.game_software_description_repository_impl import GameSoftwareDescriptionRepositoryImpl
from game_software.repository.game_software_image_repository_impl import GameSoftwareImageRepositoryImpl
from game_software.repository.game_software_price_repository_impl import GameSoftwarePriceRepositoryImpl
from game_software.repository.game_software_repository_impl import GameSoftwareRepositoryImpl
from game_software.service.game_software_service import GameSoftwareService


class GameSoftwareServiceImpl(GameSoftwareService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__gameSoftwareRepository = GameSoftwareRepositoryImpl.getInstance()
            cls.__instance.__gameSoftwarePriceRepository = GameSoftwarePriceRepositoryImpl.getInstance()
            cls.__instance.__gameSoftwareDescriptionRepository = GameSoftwareDescriptionRepositoryImpl.getInstance()
            cls.__instance.__gameSoftwareImageRepository = GameSoftwareImageRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def requestList(self, page, perPage):
        return self.__gameSoftwareRepository.list(page, perPage)

    def createGameSoftware(self, title, price, description, image):
        with transaction.atomic():
            savedGameSoftware = self.__gameSoftwareRepository.create(title)
            self.__gameSoftwarePriceRepository.create(savedGameSoftware, price)
            self.__gameSoftwareDescriptionRepository.create(savedGameSoftware, description)
            self.__gameSoftwareImageRepository.create(savedGameSoftware, image)