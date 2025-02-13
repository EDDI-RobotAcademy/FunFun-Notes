from mart.repository.mart_repository_impl import MartRepositoryImpl
from mart.service.mart_service import MartService


class MartServiceImpl(MartService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__martRepository = MartRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def loadFruit(self, fruitName, fruitCount):
        self.__martRepository.create(fruitName, fruitCount)

    def fruitMapList(self):
        fruitMapList = self.__martRepository.mapList()
        return {str(fruit): quantity for fruit, quantity in fruitMapList.items()}
