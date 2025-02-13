from order.entity.order import Order
from order.repository.order_repository import OrderRepository


class OrderRepositoryImpl(OrderRepository):
    __instance = None

    __order = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def create(self, fruitName, fruitCount, customerId):
        self.__order = Order(str(fruitName), fruitCount, customerId)

    def findOrderByCustomerId(self, customerId):
        if self.__order.getCustomerId() == customerId:
            return self.__order
