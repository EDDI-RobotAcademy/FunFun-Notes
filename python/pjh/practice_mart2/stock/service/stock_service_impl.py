from item.repository.item_repository_impl import ItemRepositoryImpl
from order.repository.order_repository_impl import OrderRepositoryImpl
from stock.repository.stock_repository_impl import StockRepositoryImpl
from stock.service.stock_service import StockService


class StockServiceImpl(StockService):
    __instance = None
    __stockList = []  # 리스트로 유지

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__stockRepository = StockRepositoryImpl.getInstance()
            cls.__instance.__itemRepository = ItemRepositoryImpl.getInstance()
            cls.__instance.__orderRepository = OrderRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def addItem(self):
        self.__itemRepository.createItem()

        itemMap = self.__itemRepository.acquireItemMap()  # 새로운 아이템 가져오기

        for itemName, itemAmount in itemMap.items():
            found = False

            for stock in self.__stockList:
                if itemName in stock:
                    # 이미 존재하면 수량을 업데이트
                    stock[itemName] += itemAmount
                    found = True
                    break

            if not found:
                # 존재하지 않으면 새 딕셔너리를 추가
                self.__stockList.append({itemName: itemAmount})

    def printAddedItemMessage(self):
        addedItemMap = self.__itemRepository.acquireItemMap() # 마지막 입력된 상품 데이터
        for itemName, itemAmount in addedItemMap.items():
            print(f"{itemName}(이)가 {itemAmount}개 입고되었습니다.")

    # def reduceItemAndAmount(self):
    #
    #

    def updateStockList(self):
        return self.__stockList

itemRepo = ItemRepositoryImpl.getInstance()
stockService = StockServiceImpl.getInstance()

stockService.addItem()  # 재고 추가
stockService.printAddedItemMessage()

stockService.addItem()
stockService.printAddedItemMessage()

print(stockService.updateStockList())


