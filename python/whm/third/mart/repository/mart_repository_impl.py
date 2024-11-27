from mart.entity.mart import Mart
from mart.repository.mart_repository import MartRepository

class MartRepositoryImpl(MartRepository):
    __instance=None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance=super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance=cls()

        return cls.__instance

    def buyMart(self):
        buyName=input("무엇을 사시겠습니까?")
