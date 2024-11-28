from item.repository.item_repository import ItemRepository


class ItemRepositoryImpl(ItemRepository):
    __instance = None

    __itemMap = {}

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def createItem(self, itemname, itemamount):
        self.itemName = itemname
        self.itemAmount = itemamount

        self.__itemMap[self.itemName] = self.itemAmount

        return self.__itemMap

    def acquireItemMap(self):
        return self.__itemMap

    def itemlist(self):
        pass

# itemList = ItemRepositoryImpl.getInstance()
# itemList.createItem("오렌지", 5)
# itemList.createItem("사과", 3)
# print(itemList.acquireItemMap())



