from buyer.repository.buyer_repositoryimpl import BuyerRepositoryImpl
from fruit.repository.fruit_repository_impl import FruitRepositoryImpl
from buyer.service.buyer_service import BuyerService

class BuyerServiceImpl(BuyerService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__buyerRepository = BuyerRepositoryImpl.getInstance()
            cls.__instance.__fruitRepository = FruitRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def buyFruit(self, fruitName, fruitCount):
        if fruitName not in self.__fruitRepository.get_fruit_name_list():
            print(f"Error: {fruitName} is not available in the inventory.")
            return
        index = self.__fruitRepository.get_fruit_name_list().index(fruitName)
        available_count = self.__fruitRepository.get_fruit_count_list()[index]

        if fruitCount > available_count:
            print(f"Error: Not enough {fruitName} available. Only {available_count} in stock.")
            return

        self.__fruitRepository.fruitCountList[index] -= fruitCount
        print(f"Success: {fruitCount} {fruitName}(s) purchased.")