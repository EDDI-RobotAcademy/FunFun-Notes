from fruit.entity.fruit import Fruit
from fruit.repository.fruit_repository import FruitRepository

class FruitRepositoryImpl(FruitRepository):
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

    def create(self, fruitName, fruitCount):
        pass

print("here")