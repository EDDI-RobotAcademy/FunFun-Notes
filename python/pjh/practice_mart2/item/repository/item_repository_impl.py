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

    def createItem(self):
        self.__itemMap = {}
        self.itemName = input("입고할 상품을 입력하세요: ")
        self.itemAmount = int(input("입고할 수량을 입력하세요: "))
        self.__itemMap[self.itemName] = self.itemAmount

    def acquireItemMap(self):
        return self.__itemMap

# itemList = ItemRepositoryImpl.getInstance()
# itemList.createItem()
#
# print(itemList.acquireItemMap())


