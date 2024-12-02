from mart.mart_entity.mart_entity import Mart
from mart.mart_repository.mart_repository import MartRepository


class MartRepositoryImpl(MartRepository):
    __instance = None
    __mart = Mart()

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def addFruit(self, fruitName, amount):
        print(f"fruitNmae={fruitName}, amount= {amount}")
        self.__mart.addFruit(fruitName,amount)

    def printCurrentStatus(self):
        fruitMap = self.__mart.getFruitMap()
        print(f"FruitMap = {fruitMap}")
