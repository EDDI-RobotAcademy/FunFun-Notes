from fruit.repository.fruit_repository_impl import FruitRepositoryImpl
from mart.service.mart_service import MartService
from mart.repository.mart_repository_impl import MartRepositoryImpl

class MartServiceImpl(MartService):
    __instance=None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance=super().__new__(cls)

            cls.__instance.__fruitRepository=FruitRepositoryImpl.getInstance()
            cls.__instance.__martRepository=MartRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance=cls()

        return cls.__instance

    def chart(self):
        chart=self.__fruitRepository.createFruit()
        buy=self.__fruitRepository.getName()

        for fruit in chart:
            if fruit==buy:
                print(buy,"사시겠습니까?")


