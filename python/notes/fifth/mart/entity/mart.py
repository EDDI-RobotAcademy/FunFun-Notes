class Mart:
    __fruitMap = {}

    def updateFruit(self, fruitName, quantity):
        if fruitName in self.__fruitMap:
            self.__fruitMap[fruitName] += quantity
            return

        self.__fruitMap[fruitName] = quantity

    def getFruitMap(self):
        return self.__fruitMap
