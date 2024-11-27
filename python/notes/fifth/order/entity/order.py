class Order:
    def __init__(self, fruitName, quantity, customerId):
        self.__fruitName = fruitName
        self.__quantity = quantity
        self.__customerId = customerId

    def getFruitName(self):
        return self.__fruitName

    def getQuantity(self):
        return self.__quantity

    def getCustomerId(self):
        return self.__customerId
