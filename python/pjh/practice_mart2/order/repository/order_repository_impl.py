from order.repository.order_repository import OrderRepository


class OrderRepositoryImpl(OrderRepository):
    __instance = None
    __orderMap = {}


    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def orderItem(self):
        self.itemName = input("주문할 상품을 입력하세요: ")
        self.orderAmount = int(input("주문할 수량을 입력하세요: "))
        self.__orderMap[self.itemName] = self.orderAmount

    def acquireOrderMap(self):
        return self.__orderMap


# orderList = OrderRepositoryImpl.getInstance()
# orderList.orderItem()
#
# print(orderList.acquireOrderMap())



