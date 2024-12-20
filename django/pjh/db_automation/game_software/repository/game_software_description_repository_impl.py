from game_software.entity.game_software_description import GameSoftwareDescription
from game_software.repository.game_software_description_repository import GameSoftwareDescriptionRepository


class GameSoftwareDescriptionRepositoryImpl(GameSoftwareDescriptionRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def create(self, gameSoftware, description):
        return GameSoftwareDescription.objects.create(gameSoftware=gameSoftware, description=description)
