from game_software.entity.game_software_price import GameSoftwarePrice
from game_software.repository.game_software_price_repository import GameSoftwarePriceRepository


class GameSoftwarePriceRepositoryImpl(GameSoftwarePriceRepository):
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

    def create(self, gameSoftware, price):
        return GameSoftwarePrice.objects.create(gameSoftware=gameSoftware, price=price)