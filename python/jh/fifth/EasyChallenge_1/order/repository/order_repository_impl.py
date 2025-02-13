from order.repository.order_repository import OrderRepository
from fruit_mart.entity.fruit_mart import FruitMart


class OrderRepositoryImpl(OrderRepository):

    __instance = None
    __fruit = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def createOrder(self, fruit, count):
        self.__fruit = fruit
        self.__count = count
        self.__fruit.updateFruitCountMap(fruit, count)

    def finishOrder(self):
        pass