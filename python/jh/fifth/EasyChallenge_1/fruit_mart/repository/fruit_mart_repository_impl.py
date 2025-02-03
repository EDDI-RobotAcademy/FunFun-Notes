from fruit_mart.entity.fruit_mart import FruitMart
from fruit_mart.repository.fruit_mart_repository import FruitMartRepository


class FruitMartRepositoryImpl(FruitMartRepository):

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


    def fruit_stock(self):
        return FruitMart.getFruitCountMap()
