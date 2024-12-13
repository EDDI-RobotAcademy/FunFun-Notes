from stock.repository.stock_repository import PayRepository


class PayRepositoryImpl(PayRepository):
    __instance = None

    __stockList = {}

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
        itemName = input("주문할 상품을 입력하세요: ")
        orderAmount = input("주문할 수량을 입력하세요: ")
        print(f"{itemName}이 {orderAmount}개 주문되었습니다.")

    def updateStockList(self):
        for


