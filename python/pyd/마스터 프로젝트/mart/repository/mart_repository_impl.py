from mart.entity.mart import Mart
from mart.repository.mart_repository import MartRepository


class MartRepositoryImpl(MartRepository):
    __instance = None
    __mart=Mart()

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def addFruit(self, fruitName, fruitAmount):
        print(f"Adding {fruitName} with amount {fruitAmount}")
        self.__mart.addFruit(fruitName, fruitAmount)

    def printCurrentStatus(self):
        fruitMap = self.__mart.getFruitMap()
        print(f"fruitMap: {fruitMap}")

