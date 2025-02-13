from fruit_mart.entity.fruit_mart import FruitMart
from customer.repository.customer_repository import CustomerRepository


class CustomerRepositoryImpl(CustomerRepository):
    __instance = None
    __fruitList = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def selectFruit(self):
        self.fruitList = FruitMart.getFruitCountMap().keys()
        print(fruitListKey)
        fruit = input("select fruit:")

    def selectCount(self):
        count = int(input("select count of fruit: "))
        return count

