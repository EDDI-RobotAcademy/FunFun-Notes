from stock.repository.stock_repository_impl import BuyerRepositoryImpl
from item.repository.item_repository_impl import ItemRepositoryImpl
from pay.repository.pay_repository_impl import PayRepositoryImpl
from pay.service.pay_service import PayService


class PayServiceImpl(PayService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__payRepository = PayRepositoryImpl.getInstance()
            cls.__instance.__itemRepository = ItemRepositoryImpl.getInstance()
            cls.__instance.__buyerRepository = BuyerRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def createOrderList(self):
        self.__orderList = []
        itemList = self.__itemRepository.acquireItemMap()
        buyerList = self.__buyerRepository.acquireBuyerMap()
        self.__orderList.extend([itemList, buyerList])

        return self.__orderList



payService = PayServiceImpl.getInstance()
billList = payService.createOrderList()

print(billList)

# def reduceItemAmount(self):
#     for