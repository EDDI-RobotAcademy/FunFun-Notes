from stock.repository.stock_repository import BuyerRepository


class BuyerRepositoryImpl(BuyerRepository):
    __instance = None

    __chosenItemMap = {}

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def chooseItem(self, itemName, itemAmount):
        self.itemName = itemName
        self.itemAmount = itemAmount

        self.__chosenItemMap[self.itemName] = self.itemAmount

        return self.__chosenItemMap

    def acquireBuyerMap(self):
        return self.__chosenItemMap

    def buyerlist(self):
        pass

# buyerList = BuyerRepositoryImpl.getInstance()
# buyerList.chooseItem("오렌지", 3)
# buyerList.chooseItem("사과", 3)
#
# print(buyerList.acquireBuyerMap())



