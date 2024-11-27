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

    def setItemName(self):
        itemName = input("상품의 이름을 입력하세요: ")
        return itemName

    def setItemAmount(self):
        itemAmount = int(input("상품의 개수를 입력하세요: "))
        return itemAmount

    def createItem(self):
        itemName = self.setItemName()
        itemAmount = self.setItemAmount()

        self.__itemMap[itemName] = itemAmount

        return self.__itemMap

    def itemlist(self):
        pass



