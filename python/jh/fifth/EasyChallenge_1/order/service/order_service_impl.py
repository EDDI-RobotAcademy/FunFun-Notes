from customer.repository.customer_repository_impl import CustomerRepositoryImpl
from fruit_mart.repository.fruit_mart_repository_impl import FruitMartRepositoryImpl
from order.repository.order_repository_impl import OrderRepositoryImpl
from order.service.order_service import OrderService


class OrderServiceImpl(OrderService):

    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__orderRepository = OrderRepositoryImpl.getInstance()
            cls.__instance.__customerRepository = CustomerRepositoryImpl.getInstance()
            # cls.__instance.__martRepository = MartRepositoryImpl.getInstance()
            cls.__instance.__fruitRepository = FruitMartRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance


    def createOrder(self):
        customer = self.__customerRepository
        selectedFruit = customer.selectFruit()
        selectedCount = customer.selectCount()
        self.__orderRepository.createOrder(selectedFruit, selectedCount)

    def finishOrder(self):
        pass
